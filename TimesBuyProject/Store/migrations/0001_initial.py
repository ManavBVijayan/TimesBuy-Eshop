# Generated by Django 4.2.2 on 2023-08-15 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='brand_images')),
                ('is_active', models.BooleanField(default=True)),
                ('offer_title', models.CharField(blank=True, max_length=100, null=True)),
                ('offer_percentage', models.PositiveIntegerField(blank=True, null=True)),
                ('offer_is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category_images')),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='GenderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='brand_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('brandName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.category')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.gendertype')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=250)),
                ('model_number', models.CharField(max_length=100)),
                ('dial_shape', models.TextField(max_length=50)),
                ('water_proof', models.BooleanField()),
                ('touch_screen', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Store.productvariant')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='banner_images')),
                ('brand', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.brand')),
            ],
        ),
    ]
