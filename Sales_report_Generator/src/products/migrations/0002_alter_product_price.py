# Generated by Django 4.1.1 on 2023-07-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(help_text='in US dollars $'),
        ),
    ]
