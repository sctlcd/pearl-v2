# Generated by Django 3.1.3 on 2020-12-31 11:16

# from django.db import migrations
# import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20201231_1110'),
    ]

    # operations = [
    #     migrations.AlterField(
    #         model_name='order',
    #         name='country',
    #         field=django_countries.fields.CountryField(max_length=2),
    #     ),
    # ]
    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
    ]
