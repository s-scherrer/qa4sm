# Generated by Django 2.1.7 on 2019-03-28 22:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0002_auto_20190328_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetConfiguration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference', models.BooleanField()),
                ('scaling_reference', models.BooleanField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataset_configuration', to='validator.Dataset')),
                ('filters', models.ManyToManyField(related_name='dataset_configuration', to='validator.DataFilter')),
                ('validation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataset_configuration', to='validator.ValidationRun')),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataset_configuration', to='validator.DataVariable')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataset_configuration', to='validator.DatasetVersion')),
            ],
        ),
    ]
