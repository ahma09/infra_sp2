import csv

from django.conf import settings
from django.core.management import BaseCommand
from reviews.models import (
    Category,
    Comment,
    Genre,
    Review,
    Title,
    GenreTitle
)
from users.models import User

DICT_MODEL_FILE = {
    User: 'user.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'title.csv',
    Review: 'review.csv',
    Comment: 'comment.csv',
    GenreTitle: 'title_genre.csv'
}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for model, file_csv in DICT_MODEL_FILE.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{file_csv}',
                'r',
                encoding='utf-8'
            ) as file_csv:
                reader = csv.DictReader(file_csv)
                model.objects.bulk_create(
                    model(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('Успешная загрузка'))
