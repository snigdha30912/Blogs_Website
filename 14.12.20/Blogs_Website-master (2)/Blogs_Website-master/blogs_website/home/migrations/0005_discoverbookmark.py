# Generated by Django 3.1.4 on 2020-12-14 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('home', '0004_bookmark_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscoverBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(default='No Title', max_length=264, unique=True)),
                ('url_field', models.URLField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(default='No Description', max_length=500, null=True)),
                ('image_field', models.URLField(default='none', max_length=1000)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
