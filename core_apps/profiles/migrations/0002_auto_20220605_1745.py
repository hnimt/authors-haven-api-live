# Generated by Django 3.2.11 on 2022-06-05 10:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default='say something about yourself', verbose_name='about me'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+250784123456', max_length=30, region=None, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='/profile_default.png', upload_to='', verbose_name='profile photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=20, verbose_name='twitter_handle'),
        ),
    ]
