# Generated by Django 2.2.5 on 2019-09-10 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20190908_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name_series',
            new_name='series',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('fantasty', 'FANTASY'), ('romance', 'ROMANCE'), ('horror', 'HORROR'), ('biographies', 'BIOGRAPHIES'), ('thrillers', 'THRILLERS'), ('sci_fi', 'SCI_FI')], max_length=15),
        ),
    ]
