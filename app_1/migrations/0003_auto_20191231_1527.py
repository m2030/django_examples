# Generated by Django 2.2.5 on 2019-12-31 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_auto_20191231_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuserinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]