
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Feed(models.Model):
    title = models.CharField(max_length=30)
    Description = models.CharField(max_length=40)
    URL = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    
    
from django.db import models

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Profile(User):
    occupation = models.CharField(max_length=30, choices=TITLE_CHOICES)
    homeIs = models.CharField(max_length=30, choices=TITLE_CHOICES)
    myHomeIsSetIn = models.CharField(max_length=30, choices=TITLE_CHOICES)
    profileAccess = models.CharField(max_length=30, choices=TITLE_CHOICES)
    style = models.CharField(max_length=30, choices=TITLE_CHOICES)
    designStyle = models.CharField(max_length=30, choices=TITLE_CHOICES)
    favoriteStyle = models.CharField(max_length=30, choices=TITLE_CHOICES)
    favoriteSpot = models.CharField(max_length=30, choices=TITLE_CHOICES)
    environment = models.CharField(max_length=30, choices=TITLE_CHOICES)
    favoriteDesigner = models.CharField(max_length=30, choices=TITLE_CHOICES)
    colors = models.CharField(max_length=30, choices=TITLE_CHOICES)
    place = models.CharField(max_length=30, choices=TITLE_CHOICES)
    
    interestingPerson = models.CharField(max_length=100)
    constantSource = models.CharField(max_length=100)
    music = models.CharField(max_length=100)
    books = models.CharField(max_length=100)
    childhoodHero = models.CharField(max_length=100)
    beautifulSeason = models.CharField(max_length=30, choices=TITLE_CHOICES)
    favoriteTime = models.CharField(max_length=30, choices=TITLE_CHOICES)
    favoriteEra = models.CharField(max_length=30, choices=TITLE_CHOICES)
    amBestKnown = models.CharField(max_length=100)
    likeToBestKnown = models.CharField(max_length=100)
    believeDesign = models.CharField(max_length=100)
    alert = models.CharField(max_length=100)
    profileImage = models.FileField(upload_to="images")
    inspriringImage = models.FileField(upload_to="images")