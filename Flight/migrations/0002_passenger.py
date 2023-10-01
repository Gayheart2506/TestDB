# Generated by Django 4.2.4 on 2023-09-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='Flight.flight')),
            ],
        ),
    ]
