# Generated by Django 3.1.4 on 2021-06-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_extraproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('processor', models.CharField(max_length=100)),
                ('screen', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='BasicProduct',
            new_name='BasicPhone',
        ),
        migrations.RenameModel(
            old_name='ExtraProduct',
            new_name='ExtraPhone',
        ),
        migrations.RenameModel(
            old_name='Tag',
            new_name='PhoneTag',
        ),
    ]