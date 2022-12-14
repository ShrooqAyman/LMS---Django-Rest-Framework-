# Generated by Django 4.1 on 2022-08-19 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Shelfs',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255)),
                ('title', models.CharField(max_length=50, null=True)),
                ('isbn', models.CharField(max_length=50, null=True)),
                ('author', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('non-available', 'non-available')], max_length=50, null=True)),
                ('image', models.ImageField(default='person.png', upload_to='images/')),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.category')),
                ('shelf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.shelf')),
            ],
            options={
                'verbose_name_plural': 'Books',
                'ordering': ('-created',),
            },
        ),
    ]
