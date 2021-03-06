# Generated by Django 3.2.6 on 2021-08-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_userdetails_user_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('mail_id', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='user_details',
        ),
    ]
