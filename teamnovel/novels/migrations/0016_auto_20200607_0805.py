# Generated by Django 2.2.6 on 2020-06-07 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('novels', '0015_remove_publishednovel_user_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCommentNovels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(max_length=200)),
                ('PublishedNovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novels.PublishedNovel')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='publishednovel',
            name='user_comments',
            field=models.ManyToManyField(related_name='commented', through='novels.UserCommentNovels', to=settings.AUTH_USER_MODEL),
        ),
    ]
