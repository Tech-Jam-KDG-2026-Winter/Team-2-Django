from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Store, Machine, ExerciseLog

from datetime import timedelta


def top(request):
    store = Store.objects.first()

    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())

    weekly_minutes = ExerciseLog.objects.filter(
        date__gte=start_of_week,
        date__lte=today
    ).aggregate(total=Sum("minutes"))["total"] or 0

    context = {
        "store": store,
        "total_exercise": weekly_minutes,
    }
    return render(request, "top.html", context)


def menu(request):
    return render(request, "menu.html")


def machine_list(request):
    machines = Machine.objects.select_related("store").all()
    return render(request, "machines.html", {"machines": machines})



def toggle_machine_status(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)

    if machine.status == "available":
        machine.status = "busy"
    else:
        machine.status = "available"

    machine.save()
    return redirect("machine_list")


@login_required
def toggle_today_exercise(request):
    today = timezone.now().date()

    log, created = ExerciseLog.objects.get_or_create(
        user=request.user,
        date=today,
        defaults={
            "minutes": 30,
            "did_exercise": True,
        }
    )

    if not created:
        log.did_exercise = not log.did_exercise
        log.minutes = 30 if log.did_exercise else 0
        log.save()

    return redirect("top")

# ---- 週ごとの運動時間（未使用予定 混乱しないようメモ） ----

def get_weekly_exercise_minutes(user):
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())

    return ExerciseLog.objects.filter(
        user=user,
        date__gte=start_of_week,
        date__lte=today
    ).aggregate(total=Sum("minutes"))["total"] or 0