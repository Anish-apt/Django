# Generated by Django 3.1.4 on 2021-01-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('fb_link', models.CharField(max_length=255)),
                ('linkedin_link', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/slider/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='media/slider/%Y/'),
        ),
    ]
