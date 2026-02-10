from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Store, Machine, ExerciseLog
from django.http import JsonResponse


def top(request):
    stores = Store.objects.all()

    today = timezone.now().date()
    start_of_month = today.replace(day=1)

    monthly_minutes = ExerciseLog.objects.filter(
        user=request.user if request.user.is_authenticated else None,
        date__gte=start_of_month,
        date__lte=today
    ).aggregate(total=Sum("minutes"))["total"] or 0

    available_map = {}
    for store in stores:
        available_map[store.name] = Machine.objects.filter(
            store=store,
            status="available"
        ).count()

    context = {
        "stores": stores,
        "total_exercise": monthly_minutes,
        "today": today,
        "available_map": available_map,
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

    machine_image_map = {
        "ショルダープレス": "shoulder_press.png",
        "チェストプレス": "chest_press.png",
        "ラットプルダウン": "lat_pulldown.png",
        "アームカール": "arm_curl.png",
        "ディップス": "dips.png",
        "レッグプレス": "leg_press.png",
        "アブベンチ": "ab_bench.png",
        "トレッドミル": "treadmill.png",
        "バイク": "bike.png",
        "セルフエステ":"self_esthe.png",
        "マッサージチェア":"massage_chair.png",
        "セルフ脱毛": "hair_removal.png",
        "ゴルフブース": "golf_booth.png",
        "セルフホワイトニング": "whitening.png",
        "セルフネイル": "nail.png",



    }
    

    machine_with_image = [ ]
    for m in machines:
        image = None
        for key, img in machine_image_map.items():
            if key in m.name:
                image = img
                break

        machine_with_image.append({
            "obj": m,
            "image": image,
        })


    context = {
        "store": store,
        "machines": machines,
        "store_key": store_key,
        "available_count": available_count,
        "busy_count": busy_count,
        "machine_image_map": machine_image_map,
    }

    return render(request, "machines.html", context)

def account(request):
    return render(request, "account.html")


def help_view(request):
    return render(request, "help.html")


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
        add_minutes = int(request.POST.get("minutes", 0))

        if add_minutes <= 0:
            return JsonResponse({"success": False})

        log, _ = ExerciseLog.objects.get_or_create(
            user=request.user,
            date=log_date,
            defaults={"minutes": 0, "did_exercise": False}
        )

        log.minutes += add_minutes
        log.did_exercise = True
        log.save()

        return JsonResponse({
            "success": True,
            "added": add_minutes,
        })

    return JsonResponse({"success": False})