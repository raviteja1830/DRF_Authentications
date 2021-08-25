# Generated by Django 3.2.5 on 2021-08-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_auth_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Game_Name', models.CharField(blank=True, max_length=50)),
                ('Game_Content', models.TextField(blank=True)),
                ('Game_Type', models.CharField(choices=[('Battle Royale', 'battle royale'), ('Areans', 'areans'), ('RPG', 'rpg'), ('SC_FI', 'sc_fi'), ('Horror', 'horror')], default='Battle royale', max_length=50)),
                ('Game_Image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
