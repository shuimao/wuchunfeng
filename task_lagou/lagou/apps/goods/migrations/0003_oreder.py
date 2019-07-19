# Generated by Django 2.2.3 on 2019-07-19 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_cartinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oreder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.UserInfo')),
            ],
        ),
    ]
