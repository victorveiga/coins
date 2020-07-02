# Generated by Django 3.0.7 on 2020-07-02 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.IntegerField()),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]