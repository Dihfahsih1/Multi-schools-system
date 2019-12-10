# Generated by Django 2.2.4 on 2019-12-06 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0016_auto_20191206_0734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salarypayment',
            old_name='role',
            new_name='role_type',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='school',
        ),
        migrations.AddField(
            model_name='salarypayment',
            name='payment_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
