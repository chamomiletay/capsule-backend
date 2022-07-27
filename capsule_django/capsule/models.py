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
        TOP = 'Top'
        BTM = 'Bottoms'
        DRESS = 'Dress'
        JMPST = 'Jumpsuit/Romper'
        SWTR = 'Sweater'
        CRDGN = 'Cardigan'
        OTRWR = 'Outerwear'
        BDYST = 'Bodysuit'
        LNGRE = 'Lingerie'
        SHOES = 'Shoes'
        ACCSRY = 'Accessory'
        SOCKS = 'Socks/Tights'

    #---- define clothing categories ----
    class CategoryType(models.TextChoices):
        LNGEWR = 'Loungewear'
        CSUL = 'Casual'
        FRML = 'Formal'
        PRTY = 'Party'
        WRK = 'Work'


    #---- define clothing color options ----
    class Color(models.TextChoices):
        RED = 'Red'
        ORNGE = 'Orange'
        YLW = 'Yellow'
        BLUE = 'Blue'
        GRN = 'Green'
        WHITE = 'White'
        BGE = 'Beige'
        CREAM = 'Cream'
        BLK = 'Black'
        PRPLE = 'Purple'
        PNK = 'Pink'
        GRAY = 'Gray'
        BRWN = 'Brown'
        TAN = 'Tan'
        MLTI = 'Multi'

    # uuid = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4)
    user = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=15, choices=Color.choices, default=Color.RED)
    # image = models.ImageField(upload_to='images/', default='')
    article_type = models.CharField(max_length=15, choices=ArticleType.choices, default=ArticleType.TOP)
    category = models.CharField(max_length=15, choices=CategoryType.choices, default=CategoryType.LNGEWR)
    brand = models.CharField(max_length=255)
    quantity = models.IntegerField()

    #---- display model instance ----
    def __str__(self):
        return self.name

# --- 