# Generated by Django 4.1.7 on 2023-04-04 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_member_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_accept',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.AddField(
            model_name='member',
            name='amount_accepted',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='member',
            name='average_order_time',
            field=models.FloatField(default=1.4),
        ),
        migrations.AddField(
            model_name='member',
            name='max_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='min_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='order_count',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='member',
            name='purchase_count',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.FloatField(default=1057800.45)),
                ('status', models.BooleanField(default=True)),
                ('date_started', models.DateTimeField(null=True)),
                ('date_finished', models.DateTimeField(null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_buyer', to='main.member')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('members', models.ManyToManyField(to='main.member')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_seller', to='main.member')),
            ],
        ),
    ]
