# Generated by Django 4.0.5 on 2022-06-05 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_rename_autor_livro_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='Author',
            new_name='author',
        ),
    ]
