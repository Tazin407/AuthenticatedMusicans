# Generated by Django 4.2.7 on 2024-01-01 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musician', to='musician.musician')),
            ],
        ),
    ]