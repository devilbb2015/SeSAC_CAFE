from django.shortcuts import render

# Create your views here.
def signin(request):


    context = {

    }

    return render(request, 'sign/signin.html', context)