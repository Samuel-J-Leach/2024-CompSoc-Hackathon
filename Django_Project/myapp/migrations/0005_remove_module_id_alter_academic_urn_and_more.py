# Generated by Django 5.0.2 on 2024-03-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_academic_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='id',
        ),
        migrations.AlterField(
            model_name='academic',
            name='URN',
            field=models.CharField(default='0000000', max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='academic',
            name='preference',
            field=models.CharField(choices=[('none', 'none'), ('robotics', 'robotics'), ('AI', 'AI'), ('cyber security', 'cyber security'), ('web development', 'web development'), ('databases', 'databases'), ('software engineering', 'software engineering'), ('electronic engineering', 'electronic engineering'), ('programming', 'programming'), ('circuit design', 'circuit design'), ('game development', 'game development')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='convener',
            name='URN',
            field=models.CharField(default='0000000', max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='module',
            name='MODULE_ID',
            field=models.CharField(default='', help_text='Three letters followed by four integers, e.g., ABC1234', max_length=7, primary_key=True, serialize=False),
        ),
    ]
