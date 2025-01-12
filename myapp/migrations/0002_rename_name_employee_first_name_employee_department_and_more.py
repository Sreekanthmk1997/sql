# Generated by Django 5.0 on 2024-08-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(default='general', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='general', max_length=100),
            preserve_default=False,
        ),
    ]
