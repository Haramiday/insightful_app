# Generated by Django 4.2.6 on 2023-10-21 00:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_blog_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='snippet',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
