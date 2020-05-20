# Generated by Django 3.0.6 on 2020-05-20 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aut',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Aut')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='blog/images')),
                ('Description', models.TextField()),
                ('facebook_link', models.CharField(max_length=10000)),
                ('linkedin_link', models.CharField(max_length=10000)),
                ('twitter_link', models.CharField(max_length=10000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Aut')),
            ],
        ),
    ]
