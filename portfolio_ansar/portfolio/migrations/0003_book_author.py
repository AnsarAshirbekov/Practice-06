# Generated by Django 5.1.2 on 2024-10-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_book_description_book_pages_book_published_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
