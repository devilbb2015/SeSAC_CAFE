"""SeSAC_CAFE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import main.views

## http://127.0.0.1:8000/main/
urlpatterns = [
    path('', main.views.index, name='index'),
    path('/guCount', main.views.guCount, name='fuCount'),
    # path('/footer', main.views.footer, name='footer'),

    path('/chart', main.views.chart, name='chart'),
    path('/api/chart1/data', main.views.chartData.as_view(), name="chartData"),

    # path('/result', main.views.result_detail, name='result_detail'),


]


