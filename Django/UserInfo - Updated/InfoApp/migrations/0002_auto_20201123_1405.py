# Generated by Django 3.1.3 on 2020-11-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstName',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(max_length=264),
        ),
    ]
