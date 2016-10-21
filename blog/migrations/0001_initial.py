# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u7c7b\u522b\u540d\u5b57')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='\u6587\u7ae0\u6807\u9898', max_length=200, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xa5\xe6\x9c\x9f')),
                ('post_file', models.FileField(upload_to=b'upload', verbose_name='\u6587\u4ef6')),
                ('views', models.IntegerField(default=0, editable=False, verbose_name='\u9605\u8bfb\u6570\u91cf')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.Category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
