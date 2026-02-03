from django.core.management.base import BaseCommand
from faker import Faker
from app.models import Store, Machine


class Command(BaseCommand):
    help = 'マシンのダミーデータを作成します'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker('ja_JP')

        store, _ = Store.objects.get_or_create(name="サンプル店")

        for i in range(total):
            Machine.objects.create(
                store=store,
                name=f"マシン{i+1}",
                status="available",
                difficulty=fake.random_element(
                    elements=["beginner", "middle"]
                )
            )

        self.stdout.write(self.style.SUCCESS(f'{total}件作成しました'))