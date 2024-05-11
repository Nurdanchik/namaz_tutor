# Generated by Django 5.0.6 on 2024-05-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(default='media/none.png', upload_to='media/')),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
    ]