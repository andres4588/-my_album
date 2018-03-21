# Generated by Django 2.0.3 on 2018-03-15 00:29

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No title', max_length=50)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('favorite', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('Categoriy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.Category')),
            ],
        ),
    ]