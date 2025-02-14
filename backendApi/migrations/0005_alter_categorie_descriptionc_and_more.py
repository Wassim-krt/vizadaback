# Generated by Django 5.0.6 on 2024-06-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApi', '0004_categorie_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='Descriptionc',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='Nomcategorie',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='link',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Descriptionc',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='course',
            name='Nomc',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='link',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='souscategorie',
            name='Nomsouscategorie',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='typeS',
            field=models.CharField(choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')], default='monthly', max_length=50),
        ),
    ]
