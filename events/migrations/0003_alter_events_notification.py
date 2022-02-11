# Generated by Django 3.2.12 on 2022-02-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_events_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='notification',
            field=models.CharField(choices=[('За час', 1), ('За два часа', 2), ('За 4 часа', 4), ('За день', 24), ('За неделю', 168)], default=None, max_length=255, null=True),
        ),
    ]
