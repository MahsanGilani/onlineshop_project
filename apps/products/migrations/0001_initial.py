# Generated by Django 5.0.1 on 2024-01-16 13:38

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted at')),
                ('restored_at', models.DateTimeField(blank=True, null=True, verbose_name='Restored at')),
                ('category_name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('category_image', models.ImageField(upload_to='categories_img/', verbose_name='Category image')),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True, verbose_name='Slug')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='products.category', verbose_name='Sub Categories')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted at')),
                ('restored_at', models.DateTimeField(blank=True, null=True, verbose_name='Restored at')),
                ('product_name', models.CharField(max_length=150, verbose_name='Product Name')),
                ('product_price', models.PositiveIntegerField(verbose_name='Product Price')),
                ('product_quantity', models.PositiveIntegerField(verbose_name='Product Quantity')),
                ('product_discount', models.PositiveIntegerField(blank=True, null=True, verbose_name='Product Discount')),
                ('discount_valid_from', models.DateField(blank=True, null=True, verbose_name='Discount Valid From')),
                ('discount_valid_to', models.DateField(blank=True, null=True, verbose_name='Discount Valid To')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='Product Video')),
                ('is_active', models.BooleanField(verbose_name='Is Active')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Product Description')),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True, verbose_name='Slug')),
                ('thumbnail', models.ImageField(upload_to='product_img/', verbose_name='Product thumbnail')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('product_name',),
                'default_manager_name': 'actives',
            },
            managers=[
                ('actives', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted at')),
                ('restored_at', models.DateTimeField(blank=True, null=True, verbose_name='Restored at')),
                ('image', models.ImageField(upload_to='product_img/', verbose_name='Product thumbnail')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_products', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['category_name'], name='products_ca_categor_d63022_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['product_name'], name='products_pr_product_097795_idx'),
        ),
    ]
