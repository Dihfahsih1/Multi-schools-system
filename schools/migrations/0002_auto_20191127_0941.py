# Generated by Django 2.2.4 on 2019-11-27 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='gross_amount',
            new_name='bank_Name',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_number',
            new_name='cheque_Number',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='date',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='is_discount_applicable',
        ),
        migrations.AddField(
            model_name='feetype',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Classroom'),
        ),
        migrations.AddField(
            model_name='feetype',
            name='classroom_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='net_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='paid_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_Method',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Cheque', 'Cheque')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='Bank_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='Bonus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='Cheque_Number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='Expenditure_Head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.ExpenditureHead'),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='Month',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='Payment_Method',
            field=models.CharField(blank=True, choices=[('Cheque', 'Cheque'), ('MobileMoney', 'MobileMoney'), ('Cash', 'Cash')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='Penalty',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='academic_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Year'),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='over_time_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='over_time_total_hour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='payee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salarygrade',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.School'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='feetype',
            name='fee_type',
            field=models.CharField(choices=[('GeneralFee', 'GeneralFee'), ('Hostel', 'Hostel'), ('Transport', 'Transport')], max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Classroom'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fee_discount', to='schools.Student'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='fee_amount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fee_am', to='schools.FeeType'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='fee_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fee', to='schools.FeeType'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='month',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paid_status',
            field=models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='use', to='schools.Student'),
        ),
        migrations.AlterField(
            model_name='salarygrade',
            name='gross_salary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='salarygrade',
            name='net_salary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='salarygrade',
            name='total_allowance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='salarygrade',
            name='total_deduction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Discount'),
        ),
        migrations.CreateModel(
            name='StudentPaidFees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_amount', models.IntegerField(default=0)),
                ('payment_Method', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Cheque', 'Cheque')], max_length=100, null=True)),
                ('bank_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('cheque_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(max_length=100)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Student')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Employee')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Role')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlySalaryPaid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('employees_id', models.CharField(default='id', max_length=100)),
                ('employee', models.CharField(max_length=100)),
                ('grade_name', models.CharField(max_length=100)),
                ('basic_salary', models.CharField(max_length=100)),
                ('house_rent', models.CharField(max_length=100)),
                ('transport_allowance', models.CharField(max_length=100)),
                ('medical_allowance', models.CharField(max_length=100)),
                ('over_time_hourly_pay', models.CharField(max_length=100)),
                ('provident_fund', models.CharField(max_length=100)),
                ('hourly_rate', models.CharField(max_length=100)),
                ('total_allowance', models.CharField(max_length=100)),
                ('total_deduction', models.CharField(max_length=100)),
                ('gross_salary', models.CharField(max_length=100)),
                ('net_salary', models.CharField(max_length=100)),
                ('over_time_total_hour', models.CharField(max_length=100)),
                ('over_time_amount', models.CharField(max_length=100)),
                ('Bonus', models.CharField(max_length=100)),
                ('Penalty', models.CharField(max_length=100)),
                ('Month', models.CharField(max_length=100)),
                ('Payment_Method', models.CharField(max_length=100)),
                ('bank_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('cheque_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('academic_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Year')),
                ('expenditure_Head', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.ExpenditureHead')),
            ],
        ),
    ]
