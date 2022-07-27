# Generated by Django 4.0.6 on 2022-07-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0019_alter_article_article_type_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(choices=[('Top', 'Top'), ('Bottoms', 'Bottoms'), ('Dress', 'Dress'), ('Jumpsuit/Romper', 'Jumpsuit/Romper'), ('Sweater', 'Sweater'), ('Cardigan', 'Cardigan'), ('Outerwear', 'Outerwear'), ('Bodysuit', 'Bodysuit'), ('Lingerie', 'Lingerie'), ('Shoes', 'Shoes'), ('Accessory', 'Accessory'), ('Socks/Tights', 'Socks/Tights')], default='ArticleType.TOP', max_length=15),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Loungewear', 'Loungewear'), ('Casual', 'Casual'), ('Formal', 'Formal'), ('Party', 'Party'), ('Work', 'Work')], default='CategoryType.WRK', max_length=15),
        ),
        migrations.AlterField(
            model_name='article',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Green', 'Green'), ('White', 'White'), ('Beige', 'Beige'), ('Cream', 'Cream'), ('Black', 'Black'), ('Purple', 'Purple'), ('Pink', 'Pink'), ('Gray', 'Gray'), ('Brown', 'Brown'), ('Tan', 'Tan'), ('Multi', 'Multi')], default='Color.RED', max_length=15),
        ),
    ]
