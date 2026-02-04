from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Store, Machine, ExerciseLog


def top(request):
    store = Store.objects.first()

    today = timezone.now().date()
    start_of_month = today.replace(day=1)

    monthly_minutes = ExerciseLog.objects.filter(
        user=request.user if request.user.is_authenticated else None,
        date__gte=start_of_month,
        date__lte=today
    ).aggregate(total=Sum("minutes"))["total"] or 0

    context = {
        "store": store,
        "total_exercise": monthly_minutes,
        "today": today,
    }
    return render(request, "top.html", context)


def menu(request):
    return render(request, "menu.html")


def machine_list(request):
    store_key = request.GET.get("store", "gotanda")

    store_map = {
        "gotanda": "五反田店",
        "meguro": "目黒店",
        "osaki": "大崎店",
    }

    store_name = store_map.get(store_key, "五反田店")
    store = get_object_or_404(Store, name=store_name)

    machines = (
        Machine.objects
        .filter(store=store)
        .order_by("status", "name")
    )

    available_count = machines.filter(status="available").count()
    busy_count = machines.filter(status="busy").count()

    context = {
        "store": store,
        "machines": machines,
        "store_key": store_key,
        "available_count": available_count,
        "busy_count": busy_count,
    }

    return render(request, "machines.html", context)

def account(request):
    return render(request, "account.html")


def toggle_machine_status(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)

    machine.status = "busy" if machine.status == "available" else "available"
    machine.save()

    store_key = request.GET.get("store", "gotanda")
    return redirect(f"/machines/?store={store_key}")

@login_required
def add_exercise_log(request):
    if request.method == "POST":
        log_date = request.POST.get("date")
        minutes = int(request.POST.get("minutes", 0))

        ExerciseLog.objects.update_or_create(
            user=request.user,
            date=log_date,
            defaults={
                "minutes": minutes,
                "did_exercise": minutes > 0,
            }
        )

    return redirect("top")