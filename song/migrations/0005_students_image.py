# Generated by Django 3.0.2 on 2020-02-17 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
