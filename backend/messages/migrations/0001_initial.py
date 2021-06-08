# Generated by Django 3.1.7 on 2021-05-16 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0006_auto_20210514_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Body')),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='sent at')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('user_agent', models.CharField(blank=True, max_length=255, verbose_name='User Agent')),
                ('parent_msg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='next_messages', to='msgs.message', verbose_name='Parent message')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
        ),
        migrations.CreateModel(
            name='ClassMessege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Class', to='classes.classes', verbose_name='Class')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recipient', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
        ),
    ]