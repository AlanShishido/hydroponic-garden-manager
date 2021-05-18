from django.shortcuts import render


def consult_api(request):
    return render(request, 'index.html')
