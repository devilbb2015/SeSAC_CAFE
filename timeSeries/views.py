from django.shortcuts import render

# Create your views here.
def chart(request):
    context = {

    }

    return render(request, 'timeSeries/chart.html', context)