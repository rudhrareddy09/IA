# Generated by Django 3.1.7 on 2021-03-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0004_universityrecord_reco'),
    ]

    operations = [
        migrations.AddField(
            model_name='universityrecord',
            name='essay',
            field=models.BooleanField(null=True),
        ),
    ]
