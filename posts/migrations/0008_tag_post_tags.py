# Generated by Django 4.2.11 on 2025-07-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_category_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.tag'),
        ),
    ]
