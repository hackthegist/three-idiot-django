# Generated by Django 2.2.4 on 2019-11-28 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('summary', models.TextField()),
                ('directorNm', models.CharField(max_length=45)),
                ('genresNm', models.CharField(max_length=150)),
                ('prdtYear', models.IntegerField()),
                ('openDt', models.IntegerField()),
                ('showTm', models.IntegerField()),
                ('nationNm', models.CharField(max_length=45)),
                ('actorsNm', models.CharField(max_length=150)),
                ('watchGradeNm', models.CharField(max_length=100)),
                ('companyNmDict', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('userRating', models.CharField(max_length=45)),
                ('audiAcc', models.CharField(max_length=45)),
                ('thumbsNm', models.CharField(max_length=500)),
                ('thumbsImage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('score', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
