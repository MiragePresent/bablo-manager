# Generated by Django 2.0 on 2018-04-16 12:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='upddated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 12, 58, 48, 402982)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='quotient',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 12, 58, 48, 403649)),
        ),
        migrations.AlterField(
            model_name='quotient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quotients', to=settings.AUTH_USER_MODEL),
        ),
    ]