# Generated by Django 3.0 on 2019-06-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogSitesi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gonderi',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
