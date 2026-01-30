from django.shortcuts import render
from django.db.models import Sum
from .models import Store, Machine, ExerciseLog


def top(request):
    store = Store.objects.first()
    total_minutes = (
        ExerciseLog.objects.aggregate(total=Sum("minutes"))["total"] or 0
    )

    context = {
        "store": store,
        "total_exercise": total_minutes,
    }
    return render(request, "top.html", context)


def menu(request):
    return render(request, "menu.html")


def machine_list(request):
    machines = Machine.objects.all()
    return render(request, "machines.html", {"machines": machines})