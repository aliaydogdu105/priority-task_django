# Generated by Django 4.1.7 on 2023-02-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('priority', models.SmallIntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=3)),
                ('is_done', models.BooleanField(default=False)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
