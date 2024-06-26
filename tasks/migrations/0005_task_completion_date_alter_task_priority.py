# Generated by Django 5.0.6 on 2024-06-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_category_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'Baixa'), ('M', 'Média'), ('H', 'Alta')], default='M', max_length=1),
        ),
    ]
