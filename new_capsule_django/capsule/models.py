from django.db import models

# Create your models here.
class Article(models.Model):
    #---- define clothing choices for user to select ----
    class ArticleType(models.TextChoices):
        TOP = 'Top', 'Top'
        BTM = 'Bottoms', 'Bottoms'
        DRESS = 'Dress', 'Dress'
        JMPST = 'Jumpsuit/Romper', 'Jumpsuit/Romper'
        SWTR = 'Sweater', 'Sweater'
        CRDGN = 'Cardigan', 'Cardigan'
        OTRWR = 'Outerwear', 'Outerwear'
        BDYST = 'Bodysuit', 'Bodysuit'
        LNGRE = 'Lingerie', 'Lingerie'
        SHOES = 'Shoes', 'Shoes'
        ACCSRY = 'Accessory', 'Accessory'
        SOCKS = 'Socks/Tights', 'Socks/Tights'

    #---- define clothing categories ----
    class CategoryType(models.TextChoices):
        LNGEWR = 'Loungewear', 'Loungewear'
        CSUL = 'Casual', 'Casual'
        FRML = 'Formal', 'Formal'
        PRTY = 'Party', 'Party'
        WRK = 'Work', 'Work'

        #---- define clothing color options ----
    class Color(models.TextChoices):
        RED = 'Red', 'Red'
        ORNGE = 'Orange', 'Orange'
        YLW = 'Yellow', 'Yellow'
        BLUE = 'Blue', 'Blue'
        GRN = 'Green', 'Green'
        WHITE = 'White', 'White'
        BGE = 'Beige', 'Beige'
        CREAM = 'Cream', 'Cream'
        BLK = 'Black', 'Black'
        PRPLE = 'Purple', 'Purple'
        PNK = 'Pink', 'Pink'
        GRAY = 'Gray', 'Gray'
        BRWN = 'Brown', 'Brown'
        TAN = 'Tan', 'Tan'
        MLTI = 'Multi', 'Multi'

    user = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=15, choices=Color.choices, default='Color.RED')
    # image = models.ImageField(upload_to='images/', default='')
    article_type = models.CharField(max_length=15, choices=ArticleType.choices, default='ArticleType.TOP')
    category = models.CharField(max_length=15, choices=CategoryType.choices, default='CategoryType.WRK')
    brand = models.CharField(max_length=255)
    quantity = models.IntegerField()

    #---- display model instance ----
    def __str__(self):
        return self.name


#---- favorites model ----
class Favorite(models.Model):
    article_1 = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles_1', default='')
    article_2 = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles_2', default='')
    article_3 = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles_3', default='')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title