# Generated by Django 4.2.3 on 2024-04-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=300)),
                ('email', models.EmailField(default='example@email.com', max_length=254)),
                ('message', models.TextField(editable=False)),
            ],
        ),
    ]
