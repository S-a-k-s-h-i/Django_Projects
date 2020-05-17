# Generated by Django 2.2.11 on 2020-05-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('offer', models.BooleanField()),
                ('author_name', models.CharField(max_length=80)),
                ('categories', models.ManyToManyField(related_name='books', to='baseapp.Category')),
            ],
        ),
    ]
