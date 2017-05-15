# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delictes', '0004_auto_20170514_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delicte',
            name='denuncia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delictes.Denuncia'),
        ),
        migrations.AlterField(
            model_name='delicte',
            name='haGuanyatelBe',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='delicte',
            name='policia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuaris.Perfil'),
        ),
        migrations.AlterField(
            model_name='delicte',
            name='superheroi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supers.Superheroi'),
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='supervillano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supers.Supervillano'),
        ),
    ]