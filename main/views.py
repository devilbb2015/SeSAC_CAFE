import csv

from django.shortcuts import render

# Create your views here.
def index(request):
    year = range(1990, 2022)
    data = {
        'date': year,
        'in_count': [29, 47, 96, 168, 69, 49, 57, 45, 21, 60, 58, 53, 37, 38, 26, 40, 30, 57, 49, 100, 162, 159, 151,
                     161, 207, 195, 182, 222, 209, 219, 221, 212],
        'out_count': [19, 18, 39, 54, 93, 102, 96, 107, 70, 89, 81, 55, 67, 41, 58, 50, 31, 44, 31, 19, 53, 45, 58, 77,
                      78, 108, 130, 143, 188, 154, 181, 137]
    }
    return render(request, "main/index.html", data)


def chart2(request):
    print('=================== chart2호출됨.')
    result = []
    with open('static/year_coffee.csv', mode='r') as cafe:
        reader = csv.reader(cafe)

        for list in reader:
            result.append(list)

    print(result)
    return render(request, "main/chart2.html", {'list': result})