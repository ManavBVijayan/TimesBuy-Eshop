# Generated by Django 4.2.2 on 2023-08-15 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Userprofileapp', '0001_initial'),
        ('Cartapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='delivery_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Userprofileapp.useraddress'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
