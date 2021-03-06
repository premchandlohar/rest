# Generated by Django 3.0.7 on 2020-06-24 04:59

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
            name='Bankprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=30)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('branch', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Bankprofiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
