# Generated by Django 3.2.10 on 2021-12-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puruweb', '0003_gallary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallary',
            name='file',
            field=models.FileField(upload_to='gallary/'),
        ),
    ]