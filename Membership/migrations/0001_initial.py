# Generated by Django 4.2.3 on 2024-04-10 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('next_of_kin', models.CharField(max_length=200)),
                ('next_of_kin_phone', models.CharField(max_length=200)),
                ('reg_date', models.CharField(max_length=200)),
                ('identification', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('passport', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Membership_verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(default='None', max_length=200)),
                ('id_image', models.ImageField(upload_to='idFolder/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(default='090', max_length=200)),
                ('verification_status', models.BooleanField(default=False)),
                ('client_name', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-timestamp',),
                'index_together': {('id',)},
            },
        ),
    ]
