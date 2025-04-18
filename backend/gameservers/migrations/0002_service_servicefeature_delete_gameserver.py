# Generated by Django 5.1.7 on 2025-04-01 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameservers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('web', 'Web Hosting'), ('game', 'Game Hosting')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('discount', models.CharField(blank=True, max_length=10, null=True)),
                ('popular', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=255)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='gameservers.service')),
            ],
        ),
        migrations.DeleteModel(
            name='GameServer',
        ),
    ]
