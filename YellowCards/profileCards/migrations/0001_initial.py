# Generated by Django 3.0.2 on 2020-03-24 15:36

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=15)),
                ('home_no', models.CharField(max_length=15, null=True)),
                ('address', models.TextField()),
                ('website', models.URLField(null=True)),
                ('position', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(null=True, upload_to='media/Profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_back', models.ImageField(upload_to='media/Card/')),
                ('card_front', models.ImageField(null=True, upload_to='media/Card/')),
                ('company', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('website', models.URLField()),
                ('fax_no', models.CharField(max_length=20, null=True)),
                ('fb_link', models.URLField(null=True)),
                ('twitter_link', models.URLField(null=True)),
                ('linked_in_link', models.URLField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
