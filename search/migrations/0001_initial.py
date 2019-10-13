# Generated by Django 2.2.6 on 2019-10-13 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=200)),
                ('price_limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('search_date', models.DateTimeField(verbose_name='date searched')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amazon_identification', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='search.Search')),
            ],
        ),
    ]