# Generated by Django 3.1.2 on 2021-05-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.CharField(default='mel', max_length=3),
        ),
    ]
