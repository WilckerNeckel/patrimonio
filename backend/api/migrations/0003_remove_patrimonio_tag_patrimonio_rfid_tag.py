# Generated by Django 5.0.6 on 2024-06-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_equipamento_patrimonio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrimonio',
            name='tag',
        ),
        migrations.AddField(
            model_name='patrimonio',
            name='rfid_tag',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]