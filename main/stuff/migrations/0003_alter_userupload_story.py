# Generated by Django 3.2.6 on 2021-08-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0002_userupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userupload',
            name='story',
            field=models.TextField(blank=True),
        ),
    ]