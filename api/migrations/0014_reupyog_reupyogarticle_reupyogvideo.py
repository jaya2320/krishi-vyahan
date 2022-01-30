# Generated by Django 3.1.4 on 2022-01-29 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20211227_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReUpyog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reupyogvideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('video_link', models.URLField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reupyog')),
            ],
        ),
        migrations.CreateModel(
            name='ReupyogArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, default='default.ico', null=True, upload_to='reupyog/article_images/')),
                ('title', models.CharField(max_length=255, null=True)),
                ('link', models.URLField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reupyog')),
            ],
        ),
    ]