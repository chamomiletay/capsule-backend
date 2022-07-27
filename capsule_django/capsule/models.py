from django.db import models
import uuid

##------ brain dump ------
    #-- wardrobe clothing article elements --
        # Name
        # Color
        # Image (via image upload)
        # Article type (top, bottom, dress, etc.)
        # Category (work, loungewear, casual, etc.)
        # Brand
        # Quantity

    #-- outfit randomizer elements --
        # Articles: Wardrobe item IDs,
        # Images
        # Weather conditions
        # Clothing category (work, loungewear, etc.)

    #-- user profile elements --
        # Username
        # Password
        # Name
        # Age
        # Description
        # Favorite Outfits (select favorites from generated outfits)
        # Favorite Colors
        # Favorite Brands 

##------ end brain dump . ------


# Create your models here.


# --- wardrobe clothing articles model ---

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

    user = models.CharField(max_length=255, default='')
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

# --- 