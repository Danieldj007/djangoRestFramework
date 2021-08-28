""" from django.db import migrations, models
from django.db.models import fields

class Migration(migrations.Migration):
    initial= True

    dependencies= []

    operations =[
        migrations.CreateModel(
            name='Tutorial',
            fields = [
                ('id', models.AutoField(auto_created= True, primary_key= True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(default='',max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('published', models.BooleanField(default= False))
            ],
        ),
    ] """