from django.http import HttpResponse
from django.shortcuts import render

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

from achievements.models import ProfessionalDevelopment, Achievements
from .models import Picture


def summ(array, start: int, stop: int):
    pic = Picture.objects.all().last()
    rangeLevel = [pic.lvl_one, pic.lvl_two, pic.lvl_three]
    massive = [0, 0, 0]
    mas = 0
    for i in range(start, stop):
        for j in array:
            if j == i:
                mas += 1
        if 0 < mas <= rangeLevel[0]:
            massive[0] += 1
        if rangeLevel[0] < mas <= rangeLevel[1]:
            massive[1] += 1
        if mas > rangeLevel[1]:
            massive[3] += 1
        mas = 0
    return massive


def initImage(request):
    if 'start' in request.GET and request.GET['start'] and 'end' in request.GET and request.GET['end']:
        if int(request.GET['start']) < int(request.GET['end']):
            ach = Achievements.objects.filter(key=request.user)
            pd = ProfessionalDevelopment.objects.filter(key=request.user)
            start = int(request.GET['start'])
            stop = int(request.GET['end'])
            massiveYON = [i.date_of_receiving.year for i in ach if
                          i.the_direction_of_self_development == 'Учебно-организационное направление'] + [
                             i.date.year for i in pd if
                             i.the_direction_of_self_development == 'Учебно-организационное направление']
            massiveYON = summ(massiveYON, start, stop)
            massiveNMN = [i.date_of_receiving.year for i in ach if
                          i.the_direction_of_self_development == 'Научно-методическое направление'] + [
                             i.date.year for i in pd if
                             i.the_direction_of_self_development == 'Научно-методическое направление']
            massiveNMN = summ(massiveNMN, start, stop)
            massiveOVN = [i.date_of_receiving.year for i in ach if
                          i.the_direction_of_self_development == 'Организационно-воспитательное направление'] + [
                             i.date.year for i in pd if
                             i.the_direction_of_self_development == 'Организационно-воспитательное направление']
            massiveOVN = summ(massiveOVN, start, stop)
            fig, ax = plt.subplots(figsize=(10, 12))
            fig.suptitle('Уровни педагогического саморазвития преподавателя')
            ax.set_xticklabels(['учебно-организационное направление',
                                'научно-методическое направление',
                                'организационно воспитательное направление'],
                               horizontalalignment='center',

                               )
            ax.set_xticks([0, 1, 2, 3, 4])
            plt.ylim([0, max(max(massiveOVN, massiveNMN, massiveYON)) + 0.1])
            ax.bar(0, massiveYON[0], linewidth=3, color='cornflowerblue')
            ax.bar(0, massiveYON[1], linewidth=3, bottom=massiveYON[0], color='orange')
            ax.bar(0, massiveYON[2], linewidth=3, bottom=massiveYON[1], color='grey')
            ax.bar(1, massiveOVN[0], linewidth=3, color='cornflowerblue')
            ax.bar(1, massiveOVN[1], linewidth=3, bottom=massiveOVN[0], color='orange')
            ax.bar(1, massiveOVN[2], linewidth=3, bottom=massiveOVN[1], color='grey')
            ax.bar(2, massiveNMN[0], linewidth=3, color='cornflowerblue')
            ax.bar(2, massiveNMN[1], linewidth=3, bottom=massiveNMN[0], color='orange')
            ax.bar(2, massiveNMN[2], linewidth=3, bottom=massiveNMN[1], color='grey')
            fig.set_figwidth(20)
            ax.legend(['репродуктивно-адаптивный уровень',
                       'активно-поисковый уровень',
                       'интенсивно творческий'], shadow=True, loc='upper right',
                      )
            response = HttpResponse(content_type='image/png')
            canvas = FigureCanvasAgg(fig)
            canvas.print_png(response)

            return response
        else:
            render(request, 'initial_image.html')

    return render(request, 'initial_image.html')
