# Generated by Django 4.0.4 on 2022-05-11 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField(max_length=160)),
                ('content', models.TextField()),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/blog/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
                ('tag_item', models.ManyToManyField(related_name='tags', to='blog.blog')),
            ],
        ),
    ]