# Generated by Django 4.2.5 on 2023-11-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_cake_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='price',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]