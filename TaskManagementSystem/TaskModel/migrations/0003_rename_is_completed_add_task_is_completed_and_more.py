# Generated by Django 4.2.7 on 2023-12-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskCategoryModel', '0001_initial'),
        ('TaskModel', '0002_alter_add_task_task_assign_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_task',
            old_name='is_completed',
            new_name='Is_completed',
        ),
        migrations.RenameField(
            model_name='add_task',
            old_name='task_Description',
            new_name='Task_Description',
        ),
        migrations.RenameField(
            model_name='add_task',
            old_name='task_Title',
            new_name='Task_Title',
        ),
        migrations.RenameField(
            model_name='add_task',
            old_name='task_assign_date',
            new_name='Task_assign_date',
        ),
        migrations.AddField(
            model_name='add_task',
            name='Category',
            field=models.ManyToManyField(to='TaskCategoryModel.add_category'),
        ),
    ]
