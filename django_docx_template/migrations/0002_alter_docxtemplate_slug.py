# Generated by Django 4.0.2 on 2022-04-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_docx_template', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docxtemplate',
            name='slug',
            field=models.SlugField(blank=True, primary_key=True, serialize=False, verbose_name='Slug'),
        ),
    ]