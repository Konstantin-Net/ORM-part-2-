# Generated by Django 3.1.2 on 2021-12-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('members', models.ManyToManyField(related_name='tags', to='articles.Article')),
            ],
        ),
    ]