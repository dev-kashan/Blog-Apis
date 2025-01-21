# Generated by Django 4.2.18 on 2025-01-20 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_cart_options_alter_wishlist_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='app/images')),
                ('detail', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '02 Blog',
            },
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_attribute',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='size',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='product_attribute',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '01 Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_status',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
