# Generated by Django 5.0.2 on 2024-03-02 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_modulecourse_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academic',
            name='department',
        ),
        migrations.RenameField(
            model_name='studentmark',
            old_name='mark',
            new_name='Mark',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='modules',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='students',
        ),
        migrations.RemoveField(
            model_name='course',
            name='modules',
        ),
        migrations.RemoveField(
            model_name='module',
            name='assessments',
        ),
        migrations.RemoveField(
            model_name='module',
            name='conveners',
        ),
        migrations.RemoveField(
            model_name='module',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='student',
            name='assessments',
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='studentmark',
            name='academic',
        ),
        migrations.RemoveField(
            model_name='studentmark',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='studentmark',
            name='id',
        ),
        migrations.RemoveField(
            model_name='studentmark',
            name='student',
        ),
        migrations.AddField(
            model_name='assessment',
            name='MODULE',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='myapp.module'),
        ),
        migrations.AddField(
            model_name='convener',
            name='MODULE',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='myapp.module'),
        ),
        migrations.AddField(
            model_name='student',
            name='COURSE',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
        ),
        migrations.AddField(
            model_name='studentmark',
            name='MARK_ID',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='academic',
            name='URN',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='ASS_ID',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='convener',
            name='URN',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='COURSE_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='module',
            name='MODULE_ID',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='URN',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='ModuleCourse',
            fields=[
                ('ID', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('COURSE', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('MODULE', models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='myapp.module')),
            ],
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.AddField(
            model_name='studentmark',
            name='ACADEMIC',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.academic'),
        ),
        migrations.AddField(
            model_name='studentmark',
            name='ASSESSMENT',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='myapp.assessment'),
        ),
        migrations.AddField(
            model_name='studentmark',
            name='STUDENT',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.student'),
        ),
    ]
