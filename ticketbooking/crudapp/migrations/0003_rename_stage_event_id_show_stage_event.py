# Generated by Django 4.2.4 on 2024-12-28 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_alter_ticket_stage_event_show'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='stage_event_id',
            new_name='stage_event',
        ),
    ]
