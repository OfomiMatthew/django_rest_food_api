# Generated by Django 4.2.11 on 2024-04-10 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodApi', '0002_alter_fooditem_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='category_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='foodApi.category'),
        ),
    ]