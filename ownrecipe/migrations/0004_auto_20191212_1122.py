# Generated by Django 2.2.6 on 2019-12-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownrecipe', '0003_newuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
