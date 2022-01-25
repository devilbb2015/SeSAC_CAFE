# Generated by Django 4.0.1 on 2022-01-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('writer', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CafeCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_count', models.FloatField()),
                ('out_count', models.FloatField()),
                ('sum_count', models.IntegerField()),
                ('status_year', models.IntegerField()),
                ('status_month', models.IntegerField()),
            ],
            options={
                'db_table': 'cafe_count',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CafeFranchise',
            fields=[
                ('fran_name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('quality_up', models.IntegerField()),
                ('quality_down', models.IntegerField()),
            ],
            options={
                'db_table': 'cafe_franchise',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CafeStatus',
            fields=[
                ('cafe_id', models.AutoField(primary_key=True, serialize=False)),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('cafe_area', models.FloatField()),
                ('business', models.IntegerField()),
                ('cafe_name', models.CharField(max_length=256)),
                ('open_date', models.IntegerField()),
                ('close_date', models.IntegerField()),
                ('gu', models.CharField(max_length=256)),
                ('franchise', models.IntegerField()),
            ],
            options={
                'db_table': 'cafe_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CafeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'cafe_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommercialArea',
            fields=[
                ('comm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comm_id_name', models.CharField(blank=True, max_length=256, null=True)),
                ('comm_category', models.CharField(max_length=256)),
                ('comm_category_name', models.CharField(max_length=256)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
            options={
                'db_table': 'commercial_area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('culture_id', models.AutoField(primary_key=True, serialize=False)),
                ('culture_category', models.CharField(blank=True, max_length=256, null=True)),
                ('culture_name', models.CharField(blank=True, max_length=256, null=True)),
                ('culture_addr', models.CharField(blank=True, max_length=256, null=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
            options={
                'db_table': 'culture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('gu', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('number_20_29', models.IntegerField(db_column='20-29')),
                ('number_30_39', models.IntegerField(db_column='30-39')),
                ('number_40_49', models.IntegerField(db_column='40-49')),
                ('number_50_59', models.IntegerField(db_column='50-59')),
                ('number_60_69', models.IntegerField(db_column='60-69')),
                ('total_worker', models.IntegerField()),
                ('density', models.IntegerField()),
                ('totalpop', models.IntegerField()),
            ],
            options={
                'db_table': 'population',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('station', models.CharField(max_length=256)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('coms', models.IntegerField()),
                ('many75', models.IntegerField()),
                ('trans', models.IntegerField()),
            ],
            options={
                'db_table': 'traffic',
                'managed': False,
            },
        ),
    ]