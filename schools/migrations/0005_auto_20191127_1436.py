# Generated by Django 2.2.4 on 2019-11-27 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20191127_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salarypayment',
            name='bank_Name',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='cheque_Number',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='expenditure_Head',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='month',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='note',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='over_time_amount',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='over_time_total_hour',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='penalty',
        ),
    ]
