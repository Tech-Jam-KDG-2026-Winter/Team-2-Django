from django.core.management.base import BaseCommand
from faker import Faker
# ここを修正！ appは実際のアプリ名、Studentはモデル名
from app.models import Student 

class Command(BaseCommand):
    help = 'ダミーデータを作成します'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='作成するデータの件数')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker('ja_JP')

        for _ in range(total):
            # Student モデルに対してデータを作成
            Student.objects.create(
                name=fake.name(),
                email=fake.email(),
            )

        self.stdout.write(self.style.SUCCESS(f'{total}件のデータを作成しました！'))