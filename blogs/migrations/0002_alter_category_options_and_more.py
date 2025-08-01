# Generated by Django 5.2.4 on 2025-07-25 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('blog_image', models.ImageField(upload_to='uploads/%y/%m/%d')),
                ('short_description', models.TextField(max_length=1000)),
                ('blog_body', models.TextField(max_length=3000)),
                ('status', models.IntegerField(choices=[('draft', 'Draft'), ('public', 'Published')], default='draft')),
                ('is_feacherd', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.category')),
            ],
        ),
    ]
