# Generated by Django 5.0.6 on 2024-05-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('ARTICLE_ID', models.IntegerField(default=True, primary_key=True, serialize=False)),
                ('TITLE', models.CharField(max_length=200, null=True)),
                ('CONTENT', models.TextField(blank=True, null=True)),
                ('GENRE', models.CharField(max_length=20, null=True)),
                ('SUB_GENRE', models.CharField(max_length=20, null=True)),
                ('PREMIUM', models.BooleanField(blank=True, null=True)),
                ('AUTHOR_ID', models.CharField(max_length=20, null=True)),
                ('STATUS', models.CharField(max_length=3, null=True)),
                ('PUBLISH_TIME', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
