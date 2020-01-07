# Generated by Django 2.1.3 on 2020-01-07 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('fastrunner', '0011_auto_20191213_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_detail', models.TextField(verbose_name='报告详细信息')),
            ],
            options={
                'verbose_name': '测试报告详情',
                'db_table': 'ReportDetail',
            },
        ),
        migrations.AlterField(
            model_name='report',
            name='summary',
            field=models.TextField(verbose_name='报告基础信息'),
        ),
        migrations.AddField(
            model_name='report',
            name='summary_detail',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE,
                                       to='fastrunner.ReportDetail'),
        ),
    ]
