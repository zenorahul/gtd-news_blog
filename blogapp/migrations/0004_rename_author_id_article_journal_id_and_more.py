# Generated by Django 5.0.6 on 2024-05-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_rename_title_article_heading'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='AUTHOR_ID',
            new_name='JOURNAL_ID',
        ),
        migrations.AddField(
            model_name='article',
            name='AUDIO_BLOB',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='VIDEO_URL',
            field=models.CharField(max_length=20, null=True),
        ),
    ]