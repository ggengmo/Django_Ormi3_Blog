# Generated by Django 4.2.6 on 2023-11-01 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_rename_parent_comment_comment_nested_reply"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="nested_reply",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reply",
                to="blog.comment",
            ),
        ),
    ]
