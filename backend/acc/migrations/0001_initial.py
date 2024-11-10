# Generated by Django 5.1.1 on 2024-11-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('shipping_address', models.CharField(max_length=50)),
                ('order_history', models.CharField(max_length=50)),
                ('cart', models.CharField(max_length=60)),
                ('payment_information', models.CharField(max_length=50)),
                ('products', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
