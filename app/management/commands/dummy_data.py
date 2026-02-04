from django.core.management.base import BaseCommand
from app.models import Store, Machine


class Command(BaseCommand):
    help = "ちょこざっぷ想定の店舗別ダミーデータを作成します"

    def handle(self, *args, **kwargs):
        # ===== 既存データ削除 =====
        Machine.objects.all().delete()
        Store.objects.all().delete()

        # ===== 店舗作成 =====
        gotanda = Store.objects.create(name="五反田店")
        meguro  = Store.objects.create(name="目黒店")
        osaki   = Store.objects.create(name="大崎店")

        # ===== 共通マシン =====
        base_machines = [
            "ショルダープレス",
            "チェストプレス",
            "ラットプルダウン",
            "バイセップスカール",
            "ディップス",
            "レッグプレス",
            "アダクション",
            "アブダクション",
            "アブドミナルトレーナー",
            "アブベンチ",
        ]

        cardio = [
            "トレッドミル",
            "バイク",
        ]

        # ===== 店舗別オプション =====
        options = {
            "五反田店": [
                "セルフエステ",
                "マッサージチェア",
                "セルフ脱毛",
            ],
            "目黒店": [
                "セルフホワイトニング",
                "セルフネイル",
            ],
            "大崎店": [
                "ゴルフブース",
                "マッサージチェア",
            ],
        }

        # ===== 作成処理 =====
        for store in [gotanda, meguro, osaki]:
            # 筋トレ
            for name in base_machines:
                Machine.objects.create(
                    store=store,
                    name=name,
                    status="available",
                    difficulty="beginner",
                )

            # 有酸素（店舗差をつける）
            for name in cardio:
                Machine.objects.create(
                    store=store,
                    name=name,
                    status="available",
                    difficulty="middle",
                )

            # オプション
            for name in options.get(store.name, []):
                Machine.objects.create(
                    store=store,
                    name=name,
                    status="available",
                    difficulty="beginner",
                )

        self.stdout.write(self.style.SUCCESS("店舗別ダミーデータを作成しました"))