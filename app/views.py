# techteam2/app/views.py

from django.shortcuts import render

# TODO: トップ画面
def top(request):
    context = {

    }
    return render(request, 'machines.html', context)


def route(request):
    """
    仮のルート画面
    企画確定後に中身を調整
    """
    return render(request, 'route.html')