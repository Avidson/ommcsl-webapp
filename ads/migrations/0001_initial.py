# Generated by Django 4.2.3 on 2024-04-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Display_ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads_title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='ads/')),
                ('organisation_name', models.CharField(max_length=200)),
                ('ads_url', models.CharField(default=None, max_length=300)),
                ('ads_starts', models.DateTimeField()),
                ('ads_end', models.DateTimeField()),
            ],
        ),
    ]