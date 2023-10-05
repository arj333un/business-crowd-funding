# Generated by Django 4.1.7 on 2023-04-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('investortype', models.CharField(max_length=50)),
                ('status', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'db_table': 'investor',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('companyprofile', models.CharField(max_length=500)),
                ('domain', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'owner',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('hours', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Respond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.IntegerField()),
                ('quotedamount', models.IntegerField()),
                ('quotedby', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'respond',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(default='user', max_length=50)),
                ('status', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]