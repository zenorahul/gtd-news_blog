# Generated by Django 5.0.6 on 2024-05-17 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_rename_author_id_article_journal_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('USER_ID', models.IntegerField(default=True, primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=100, null=True)),
                ('USERNAME', models.CharField(max_length=20, unique=True)),
                ('PASSWORD', models.CharField(max_length=20, unique=True)),
                ('MAIL_ID', models.CharField(max_length=50, null=True)),
                ('AC_TYPE', models.CharField(max_length=20, null=True)),
                ('SUB_START', models.DateField(blank=True, null=True)),
                ('SUB_END', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='HEADING',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='VIDEO_URL',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='ArticleImg',
            fields=[
                ('IMG_ID', models.IntegerField(default=True, primary_key=True, serialize=False)),
                ('IMG_BLOB', models.BinaryField(null=True)),
                ('ARTICLE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.article')),
            ],
        ),
    ]
