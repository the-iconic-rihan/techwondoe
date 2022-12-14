# Generated by Django 4.1.1 on 2022-09-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("companyId", models.UUIDField(primary_key=True, serialize=False)),
                ("companyName", models.CharField(max_length=1000)),
                ("companyCeo", models.CharField(max_length=30)),
                ("companyAddress", models.CharField(max_length=1000)),
                ("inceptionDate", models.DateTimeField(auto_now_add=True)),
                ("inceptionDate2", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
