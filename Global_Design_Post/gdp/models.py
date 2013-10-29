
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Feed(models.Model):
    title = models.CharField(max_length=255)
    Description = models.CharField(max_length=40)
    URL = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
 
 
class Upload(models.Model):
    title = models.CharField(max_length=255)
    Description = models.CharField(max_length=40)
    URL = models.CharField(max_length=255)
    upload = models.FileField(upload_to="gdp/static/images/upload")      
    

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Profile(User):
    
    O_CHOICES = (
    ("I prefer not to say","I prefer not to say"),
    ("Administrative","Administrative"),
    ("Medical","Medical"),
    ("Artist/Creative/Performer ","Artist/Creative/Performer "),
    ("Sales/Marketing","Sales/Marketing "),
    ("Executive Management ","Executive Management&nbsp"),
    ("Education","Education"),
    ("Banking/Financial","Banking/Financial"),
    ("Computers","Computers"),
    ("Travel/Hospitality","Travel/Hospitality"),
    ("Legal","Legal"),
    ("Self-Employed","Self-Employed"),
    ("Architect","Architect"),
    ("Craftsman/Construction","Craftsman/Construction"),
    ("Engineer","Engineer"),
    ("Professional Trade","Professional Trade"),
    ("Homemaker","Homemaker"),
    ("Food Services","Food Services"),
    ("Military/Government/Politics","Military/Government/Politics"),
    ("Real Estate","Real Estate"),
    ("Retail","Retail&nbsp"),
    ("Retired","Retired"),
    ("Student","Student"),
    ("Unemployed","Unemployed"),
    ("Other","Other")
    )
    TYPE_CHOICES = (
    ("Urban","Urban"),
    ("Suburban","Suburban"),
    ("Small Town","Small Town"),
    ("Mountain","Mountain"),
    ("Country","Country"),
    ("Resort","Resort"),
    ("Ocean","Ocean"),
    ("Lake","Lake"))
    PROFILE_CHOICES = (
    ("Private","Private"),
    ("Public","Public"))
    COUNTRY = (
    ("Afghanistan","Afghanistan"),
    ("Aland Islands","Aland Islands"),
    ("Albania","Albania"),
    ("Algeria","Algeria"),
    ("American Samoa","American Samoa"),
    ("Andorra","Andorra"),
    ("Angola","Angola"),
    ("Anguilla","Anguilla"),
    ("Antarctica","Antarctica"),
    ("Antigua and Barbuda","Antigua and Barbuda"),
    ("Argentina","Argentina"),
    ("Armenia","Armenia"),
    ("Aruba","Aruba"),
    ("Australia","Australia"),
    ("Austria","Austria"),
    ("Azerbaijan","Azerbaijan"),
    ("Bahamas","Bahamas"),
    ("Bahrain","Bahrain"),
    ("Bangladesh","Bangladesh"),
    ("Barbados","Barbados"),
    ("Belarus","Belarus"),
    ("Belgium","Belgium"),
    ("Belize","Belize"),
    ("Benin","Benin"),
    ("Bermuda","Bermuda"),
    ("Bhutan","Bhutan"),
    ("Bolivia","Bolivia"),
    ("Bosnia and Herzegovina","Bosnia and Herzegovina"),
    ("Botswana","Botswana"),
    ("Bouvet Island","Bouvet Island"),
    ("Brazil","Brazil"),
    ("British Indian Ocean Territory","British Indian Ocean Territory"),
    ("Brunei Darussalam","Brunei Darussalam"),
    ("Bulgaria","Bulgaria"),
    ("Burkina Faso","Burkina Faso"),
    ("Burundi","Burundi"),
    ("Cambodia","Cambodia"),
    ("Cameroon","Cameroon"),
    ("Canada","Canada"),
    ("Cape Verde","Cape Verde"),
    ("Cayman Islands","Cayman Islands"),
    ("Central African Republic","Central African Republic"),
    ("Chad","Chad"),
    ("Chile","Chile"),
    ("China","China"),
    ("Christmas Island","Christmas Island"),
    ("Cocos (Keeling) Islands","Cocos (Keeling) Islands"),
    ("Colombia","Colombia"),
    ("Comoros","Comoros"),
    ("Congo","Congo"),
    ("Congo, The Democratic Republic of The","Congo, The Democratic Republic of The"),
    ("Cook Islands","Cook Islands"),
    ("Costa Rica","Costa Rica"),
    ("Cote D'ivoire","Cote D'ivoire"),
    ("Croatia","Croatia"),
    ("Cuba","Cuba"),
    ("Cyprus","Cyprus"),
    ("Czech Republic","Czech Republic"),
    ("Denmark","Denmark"),
    ("Djibouti","Djibouti"),
    ("Dominica","Dominica"),
    ("Dominican Republic","Dominican Republic"),
    ("Ecuador","Ecuador"),
    ("Egypt","Egypt"),
    ("El Salvador","El Salvador"),
    ("Equatorial Guinea","Equatorial Guinea"),
    ("Eritrea","Eritrea"),
    ("Estonia","Estonia"),
    ("Ethiopia","Ethiopia"),
    ("Falkland Islands (Malvinas)","Falkland Islands (Malvinas)"),
    ("Faroe Islands","Faroe Islands"),
    ("Fiji","Fiji"),
    ("Finland","Finland"),
    ("France","France"),
    ("French Guiana","French Guiana"),
    ("French Polynesia","French Polynesia"),
    ("French Southern Territories","French Southern Territories"),
    ("Gabon","Gabon"),
    ("Gambia","Gambia"),
    ("Georgia","Georgia"),
    ("Germany","Germany"),
    ("Ghana","Ghana"),
    ("Gibraltar","Gibraltar"),
    ("Greece","Greece"),
    ("Greenland","Greenland"),
    ("Grenada","Grenada"),
    ("Guadeloupe","Guadeloupe"),
    ("Guam","Guam"),
    ("Guatemala","Guatemala"),
    ("Guernsey","Guernsey"),
    ("Guinea","Guinea"),
    ("Guinea-bissau","Guinea-bissau"),
    ("Guyana","Guyana"),
    ("Haiti","Haiti"),
    ("Heard Island and Mcdonald Islands","Heard Island and Mcdonald Islands"),
    ("Holy See (Vatican City State)","Holy See (Vatican City State)"),
    ("Honduras","Honduras"),
    ("Hong Kong","Hong Kong"),
    ("Hungary","Hungary"),
    ("Iceland","Iceland"),
    ("India","India"),
    ("Indonesia","Indonesia"),
    ("Iran, Islamic Republic of","Iran, Islamic Republic of"),
    ("Iraq","Iraq"),
    ("Ireland","Ireland"),
    ("Isle of Man","Isle of Man"),
    ("Israel","Israel"),
    ("Italy","Italy"),
    ("Jamaica","Jamaica"),
    ("Japan","Japan"),
    ("Jersey","Jersey"),
    ("Jordan","Jordan"),
    ("Kazakhstan","Kazakhstan"),
    ("Kenya","Kenya"),
    ("Kiribati","Kiribati"),
    ("Korea, Democratic People's Republic of","Korea, Democratic People's Republic of"),
    ("Korea, Republic of","Korea, Republic of"),
    ("Kuwait","Kuwait"),
    ("Kyrgyzstan","Kyrgyzstan"),
    ("Lao People's Democratic Republic","Lao People's Democratic Republic"),
    ("Latvia","Latvia"),
    ("Lebanon","Lebanon"),
    ("Lesotho","Lesotho"),
    ("Liberia","Liberia"),
    ("Libyan Arab Jamahiriya","Libyan Arab Jamahiriya"),
    ("Liechtenstein","Liechtenstein"),
    ("Lithuania","Lithuania"),
    ("Luxembourg","Luxembourg"),
    ("Macao","Macao"),
    ("Macedonia, The Former Yugoslav Republic of","Macedonia, The Former Yugoslav Republic of"),
    ("Madagascar","Madagascar"),
    ("Malawi","Malawi"),
    ("Malaysia","Malaysia"),
    ("Maldives","Maldives"),
    ("Mali","Mali"),
    ("Malta","Malta"),
    ("Marshall Islands","Marshall Islands"),
    ("Martinique","Martinique"),
    ("Mauritania","Mauritania"),
    ("Mauritius","Mauritius"),
    ("Mayotte","Mayotte"),
    ("Mexico","Mexico"),
    ("Micronesia, Federated States of","Micronesia, Federated States of"),
    ("Moldova, Republic of","Moldova, Republic of"),
    ("Monaco","Monaco"),
    ("Mongolia","Mongolia"),
    ("Montenegro","Montenegro"),
    ("Montserrat","Montserrat"),
    ("Morocco","Morocco"),
    ("Mozambique","Mozambique"),
    ("Myanmar","Myanmar"),
    ("Namibia","Namibia"),
    ("Nauru","Nauru"),
    ("Nepal","Nepal"),
    ("Netherlands","Netherlands"),
    ("Netherlands Antilles","Netherlands Antilles"),
    ("New Caledonia","New Caledonia"),
    ("New Zealand","New Zealand"),
    ("Nicaragua","Nicaragua"),
    ("Niger","Niger"),
    ("Nigeria","Nigeria"),
    ("Niue","Niue"),
    ("Norfolk Island","Norfolk Island"),
    ("Northern Mariana Islands","Northern Mariana Islands"),
    ("Norway","Norway"),
    ("Oman","Oman"),
    ("Pakistan","Pakistan"),
    ("Palau","Palau"),
    ("Palestinian Territory, Occupied","Palestinian Territory, Occupied"),
    ("Panama","Panama"),
    ("Papua New Guinea","Papua New Guinea"),
    ("Paraguay","Paraguay"),
    ("Peru","Peru"),
    ("Philippines","Philippines"),
    ("Pitcairn","Pitcairn"),
    ("Poland","Poland"),
    ("Portugal","Portugal"),
    ("Puerto Rico","Puerto Rico"),
    ("Qatar","Qatar"),
    ("Reunion","Reunion"),
    ("Romania","Romania"),
    ("Russian Federation","Russian Federation"),
    ("Rwanda","Rwanda"),
    ("Saint Helena","Saint Helena"),
    ("Saint Kitts and Nevis","Saint Kitts and Nevis"),
    ("Saint Lucia","Saint Lucia"),
    ("Saint Pierre and Miquelon","Saint Pierre and Miquelon"),
    ("Saint Vincent and The Grenadines","Saint Vincent and The Grenadines"),
    ("Samoa","Samoa"),
    ("San Marino","San Marino"),
    ("Sao Tome and Principe","Sao Tome and Principe"),
    ("Saudi Arabia","Saudi Arabia"),
    ("Senegal","Senegal"),
    ("Serbia","Serbia"),
    ("Seychelles","Seychelles"),
    ("Sierra Leone","Sierra Leone"),
    ("Singapore","Singapore"),
    ("Slovakia","Slovakia"),
    ("Slovenia","Slovenia"),
    ("Solomon Islands","Solomon Islands"),
    ("Somalia","Somalia"),
    ("South Africa","South Africa"),
    ("South Georgia and The South Sandwich Islands","South Georgia and The South Sandwich Islands"),
    ("Spain","Spain"),
    ("Sri Lanka","Sri Lanka"),
    ("Sudan","Sudan"),
    ("Suriname","Suriname"),
    ("Svalbard and Jan Mayen","Svalbard and Jan Mayen"),
    ("Swaziland","Swaziland"),
    ("Sweden","Sweden"),
    ("Switzerland","Switzerland"),
    ("Syrian Arab Republic","Syrian Arab Republic"),
    ("Taiwan, Province of China","Taiwan, Province of China"),
    ("Tajikistan","Tajikistan"),
    ("Tanzania, United Republic of","Tanzania, United Republic of"),
    ("Thailand","Thailand"),
    ("Timor-leste","Timor-leste"),
    ("Togo","Togo"),
    ("Tokelau","Tokelau"),
    ("Tonga","Tonga"),
    ("Trinidad and Tobago","Trinidad and Tobago"),
    ("Tunisia","Tunisia"),
    ("Turkey","Turkey"),
    ("Turkmenistan","Turkmenistan"),
    ("Turks and Caicos Islands","Turks and Caicos Islands"),
    ("Tuvalu","Tuvalu"),
    ("Uganda","Uganda"),
    ("Ukraine","Ukraine"),
    ("United Arab Emirates","United Arab Emirates"),
    ("United Kingdom","United Kingdom"),
    ("United States","United States"),
    ("United States Minor Outlying Islands","United States Minor Outlying Islands"),
    ("Uruguay","Uruguay"),
    ("Uzbekistan","Uzbekistan"),
    ("Vanuatu","Vanuatu"),
    ("Venezuela","Venezuela"),
    ("Viet Nam","Viet Nam"),
    ("Virgin Islands, British","Virgin Islands, British"),
    ("Virgin Islands, U.S.","Virgin Islands, U.S."),
    ("Wallis and Futuna","Wallis and Futuna"),
    ("Western Sahara","Western Sahara"),
    ("Yemen","Yemen"),
    ("Zambia","Zambia"),
    ("Zimbabwe","Zimbabwe"))
    DESIGN_STYLE=(
    ("Art Deco","Art Deco"),
    ("Arts and Crafts","Arts and Crafts"),
    ("Cape Cod","Cape Cod"),
    ("Colonial","Colonial"),
    ("Contemporary","Contemporary"),
    ("Farmhouse","Farmhouse"),
    ("Federal","Federal"),
    ("French Provincial","French Provincial"),
    ("Greek Revival","Greek Revival"),
    ("Italianate","Italianate"),
    ("Loft","Loft"),
    ("Mediterranian","Mediterranian"),
    ("Mid-Century Modern","Mid-Century Modern"),
    ("Modern","Modern"),
    ("Neoclassical","Neoclassical"),
    ("Postwar","Postwar"),
    ("Prairie","Prairie"),
    ("Prewar","Prewar"),
    ("Pueblo Revival","Pueblo Revival"),
    ("Ranch","Ranch"),
    ("Row House","Row House"),
    ("Spanish","Spanish"),
    ("Tudor","Tudor"),
    ("Victorian","Victorian")
    )
    SPOT_CHOICES =(
                   ("On the beach","On the beach"),
                    ("In the mountains","In the mountains"),
                    ("At a campground","At a campground"),
                    ("At a Resort","At a Resort"),
                    ("Musical Festival","Musical Festival"),
                    ("On a Cruise","On a Cruise")

                   )
    occupation = models.CharField(verbose_name="Occupation",max_length=255, choices=O_CHOICES,default="I prefer not to say")
    homeIs = models.CharField(verbose_name="Home is",max_length=255, choices=COUNTRY,default="Afghanistan")
    myHomeIsSetIn = models.CharField(verbose_name="My home is set in",max_length=255, choices=TYPE_CHOICES,default="Urban")
    profileAccess = models.CharField(verbose_name="I would like my profile to be",max_length=255, choices=PROFILE_CHOICES,default="Urban")
    style = models.CharField(verbose_name="Style of your home",max_length=255, choices=DESIGN_STYLE)
    designStyle = models.CharField(verbose_name="My favourite design style",max_length=255, choices=DESIGN_STYLE)
    favoriteSpot = models.CharField(verbose_name="Favourite vacation spot",max_length=255, choices=SPOT_CHOICES)
    environment = models.CharField(verbose_name="Environment I feel most at home",max_length=255, choices=TITLE_CHOICES)
    favoriteDesigner = models.CharField(verbose_name="Favorite designer",max_length=255, choices=TITLE_CHOICES)
    colors = models.CharField(verbose_name="Colors i love",max_length=255, choices=TITLE_CHOICES)
    place = models.CharField(verbose_name="Place on earth i would most like to explore",max_length=255, choices=TITLE_CHOICES)
    
    interestingPerson = models.CharField(verbose_name="Most interesting person I have met or would like to meet",max_length=100)
    constantSource = models.CharField(verbose_name = "Most constant source of design inspiration",max_length=100)
    music = models.CharField(verbose_name = "Music that makes me move",max_length=100)
    books = models.CharField(verbose_name = "Books I love",max_length=100)
    childhoodHero = models.CharField(verbose_name = "My Childhood hero",max_length=100)
    beautifulSeason = models.CharField(verbose_name = "Most beautiful season",max_length=255, choices=TITLE_CHOICES)
    favoriteTime = models.CharField(verbose_name = "Favorite time of day",max_length=255, choices=TITLE_CHOICES)
    favoriteEra = models.CharField(verbose_name = "Favorite era",max_length=255 ,choices=TITLE_CHOICES)
    amBestKnown = models.CharField(verbose_name = "I am best known for",max_length=100)
    likeToBestKnown = models.CharField(verbose_name = "I would like to be best known for",max_length=100)
    believeDesign = models.CharField(verbose_name = "I believe design is",max_length=100)
    alert = models.CharField(verbose_name = "I would love opportunities to give through my passion or talent for design",max_length=100)
    profileImage = models.FileField(verbose_name = "Profile Image",upload_to="gdp/static/images/upload")
    inspriringImage = models.FileField(verbose_name = "Inspiring image",upload_to="gdp/static/images/upload")
    
    
    
class FeedItem(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    url = models.URLField(max_length=255)
    author = models.CharField(max_length=255)
    publishedDate = models.DateTimeField()
    updatedDate = models.DateTimeField(auto_now=True)
    
    
class Imagelist(models.Model):
    title = models.CharField(max_length=255)
    src = models.URLField(max_length=255)
    height = models.CharField(max_length=255)
    width = models.CharField(max_length=255)
    updatedDate = models.DateTimeField(auto_now=True)
    