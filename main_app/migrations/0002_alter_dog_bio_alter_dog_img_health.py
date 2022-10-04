# Generated by Django 4.1.1 on 2022-10-04 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='bio',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='dog',
            name='img',
            field=models.CharField(max_length=2000),
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('life_expectancy', models.IntegerField(default=0)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health', to='main_app.dog')),
            ],
        ),
    ]
