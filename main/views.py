import csv

from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.views.generic import View
from django.shortcuts import render
import folium

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
from main.models import CafeCount, CafeStatus


def index(request):
    qs = CafeStatus.objects.all()
    datas = qs.values()
    lat = []
    lng = []
    gu = []
    cafe_name = []

    for i in datas:
        if i['business'] == 1:
            lat.append(i['lat'])
            lng.append(i['lng'])
            gu.append(i['gu'])
            cafe_name.append(i['cafe_name'])

    context = {
        "gu": gu,
        "lat": lat,
        "lng": lng,
        "cafe_name": cafe_name,
    }

    return render(request, 'main/index.html', context)

def signin(request):

    context = {

    }

    return render(request, 'main/signin.html', context)

def board(request):

    context = {

    }

    return render(request, 'main/board.html', context)

def guCount(request):
    qs = CafeStatus.objects.all()
    datas = qs.values()
    qs2 = CafeStatus.objects.filter(franchise__lt=2)
    datas2 = qs2.values()
    gu = []
    cafe_name = []
    franchise = []

    for i in datas:
        if i['business'] == 1:
            gu.append(i['gu'])
            cafe_name.append(i['cafe_name'])

    for i in datas2:
        franchise.append(i['gu'])

    context = {
        "gu": gu,
        "cafe_name": cafe_name,
        "franchise": franchise,
    }

    return render(request, 'main/gu_count.html', context)

def chart2(request):
    print('=================== chart2호출됨.')
    result = []
    with open('static/year_coffee.csv', mode='r') as cafe:
        reader = csv.reader(cafe)

        for list in reader:
            result.append(list)

    print(result)
    return render(request, "main/chart2.html", {'list': result})


def chart(request):
    try:
        queryset = CafeCount.objects.all()
        datas = queryset.values()

        result = []
        for list in datas:
            result.append(list)

        print(result)

    except:
        print("쿼리 실행 실패")

    return render(request, 'main/chart.html', {"list": result})


class chartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        qs = CafeCount.objects.all()
        datas = qs.values()
        # print(datas)
        labels = []
        sum_count = []
        for i in datas:
            labels.append(i['status_year'])
            sum_count.append(i['sum_count'])

        data = {
            "labels": labels,
            "defaultData": sum_count,
        }
        return Response(data)



#
# def result_detail(request):
#     context = {}
#     return render(request, 'chartapp/chart.html', context)


