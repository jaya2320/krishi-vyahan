# Generated by Django 3.1.4 on 2021-12-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_seller_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
