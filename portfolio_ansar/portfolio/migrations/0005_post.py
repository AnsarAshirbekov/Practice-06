# Generated by Django 5.1.2 on 2024-10-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_book_price_book_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('subtitle', models.CharField(max_length=200)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('text', models.TextField(blank=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
