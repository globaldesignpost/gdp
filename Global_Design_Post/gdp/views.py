# Create your views here.
import os
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.shortcuts import redirect
from gdp.forms import RegistrationForm, FeedForm ,MyProfileForm,AddForm,VaultForm
from gdp.models import Feed,Upload,Outposts,Profile,FeedItem,Imagelist,Inspiration,Colors,Designs,Bazaar
from gdp.forms import RegistrationForm,PasswordReCaptchaForm
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate,login
from django.contrib import auth
from gdp.tables import FeedTable,UploadTable,FeedItemTable
from django.shortcuts import render
from django_tables2  import RequestConfig
import datetime
import feedparser
import re

def home(request):
    #from django.core.mail import send_mail
    #send_mail('Subject here', 'Here is the message.', 'from@example.com',['tomjoy002@gmail.com'], fail_silently=False)
    #from PIL import Image
    #im=Image.open('gdp/static/images/5.jpg')
    #print im.size[0]# (width,height) tuple
    #Imagelistval = Imagelist.objects.all().order_by('-id')[:100] 
    #variables = RequestContext(request, {'Imagelist':Imagelistval})
    outposts_list=Outposts.objects.all().order_by('-id')[:5]
    colors_list1=Colors.objects.all().order_by('-id')[:3]
    variables = RequestContext(request, {'colors_list1':colors_list1 ,'outposts_list':outposts_list})
    return render_to_response('index.html',variables )


def registerUser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print "tooooooooooooom"
        if form.is_valid():
            

            print "tommmmmmmmmm"
            dictParamList = {}
            dictParamList['email'] = form.cleaned_data['emailAddress'].strip()
            dictParamList['userName'] = form.cleaned_data['userName'].strip()
            dictParamList['password'] = form.cleaned_data['choosePassword'].strip()
            user = User.objects.create_user(dictParamList['userName'], dictParamList['email'], dictParamList['password'])
            user.is_staff = True
            user.save()
            return HttpResponseRedirect('/login/')
            #objUserManagementDA = usermanagementDA()
            #objUserManagementDA.createuser(dictParamList)
            #return HttpResponse('success')
            variables = RequestContext(request, {'welcomeMsg':'','form':form})
            return render_to_response('registration.html',variables )
        else:
            print "error"
            print form
            variables = RequestContext(request, {'welcomeMsg':'','form':form})
            return render_to_response('registration/registration.html',variables )
 
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'welcomeMsg':'','form':form})
        return render_to_response('registration/registration.html',variables )

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def favorites(request):
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('favourites.html',variables )

def inspiration(request):
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('inspiration.html',variables )

def colors(request):
    colors_list1=Colors.objects.all().order_by('-id')[:3]
    colors_list2=Colors.objects.all().order_by('-id')[:4]
    
    
    variables = RequestContext(request, {'colors_list1':colors_list1,'colors_list2':colors_list2})
    return render_to_response('colors.html',variables )

@login_required 
def myProfile(request):
    if request.method == 'POST':
        print request.POST
        form = MyProfileForm(request.POST, request.FILES)
        #print form
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/')
        else:
            
            
            variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','form':form})
            return render_to_response('myProfile.html',variables )
            
    else:
        print request.user.username
        #userobj = Profile.objects.get(id = request.user.id)
        from django.forms.models import model_to_dict 
        #userobjDict = model_to_dict(userobj)
        form =MyProfileForm()
        variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','form':form})
        return render_to_response('myProfile.html',variables )

def bazaar(request):
    bazaar_list=Bazaar.objects.all().order_by('-id')[:12]
    imagelist=[]
    for row in bazaar_list:
        image = {'img':row.img,'title':row.title,'url':row.url}
        imagelist.append(image)
    variables = RequestContext(request, {'imagelist':imagelist})
    return render_to_response('bazaar.html',variables )

@login_required
def mygdp(request):
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('mygdp.html',variables )

def outposts(request):
    form =MyProfileForm()
    print "1111111111111111111111111111111111111"
    try:
        outposts_list=Outposts.objects.all().order_by('-id')[:5]
    except Exception,e:
        print e
    print "111111111111111222222222221111111111111111111111"
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','form':form,'outposts_list':outposts_list})
    return render_to_response('outposts.html',variables )



def vault(request):
    form =VaultForm()
    from itertools import chain
    Outposts_list = Outposts.objects.all().order_by('-id')[:10]
    Colors_list = Colors.objects.all().order_by('-id')[:10]
    Designs_list = Designs.objects.all().order_by('-id')[:10]
    Inspiration_list = Inspiration.objects.all().order_by('-id')[:10]
    Bazaar_list = Bazaar.objects.all().order_by('-id')[:10]
    
    #result_list = sorted(chain(Outposts_list,Colors_list, Designs_list, Inspiration_list,Bazaar_list),key=lambda instance: instance.date_created)
    result_list = list(chain(Outposts_list,Colors_list, Designs_list, Inspiration_list,Bazaar_list))
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','form':form,'result_list':result_list})
    return render_to_response('vault.html',variables )

def authentication(request):
    from django.contrib.auth import authenticate
    username=request.GET.get('username','')
    password=request.GET.get('password','')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            return HttpResponse("You provided a correct username and password!")
        else:
            return HttpResponse("Your account has been disabled!")
    else:

        return HttpResponse("Your username and password were incorrect.")
    
@login_required    
def feed(request):
    if request.method == 'POST':
        add_feed = FeedForm(request.POST)
        print "tooooooooooooom"
        if add_feed.is_valid():
            add_feed.save()
            list_feed = Feed.objects.all()
            table=FeedTable(list_feed)
            RequestConfig(request, paginate={"per_page": 25}).configure(table)
            return render(request, 'feed.html', {'table': table,'add_feed':add_feed})
        else:
            list_feed = Feed.objects.all()
            table=FeedTable(list_feed)
            RequestConfig(request, paginate={"per_page": 25}).configure(table)
            return render(request, 'feed.html', {'table': table,'add_feed':add_feed})
            
    else:
        add_feed= FeedForm()
        list_feed = Feed.objects.all()
        table=FeedTable(list_feed)
        RequestConfig(request, paginate={"per_page": 25}).configure(table)
        return render(request, 'feed.html', {'table': table,'add_feed':add_feed})
    
def imagelist(request):
    list_feed = Upload.objects.all()
    table=UploadTable(list_feed)
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    return render(request, 'imagelist.html', {'table': table})

@login_required()  
def addimage(request):
    if request.method == 'POST':
        add_image = AddForm(request.POST, request.FILES)
        if add_image.is_valid():
            add_image.save()
            return HttpResponseRedirect('/imagelist/')
            #RequestConfig(request, paginate={"per_page": 25}).configure(table)
            #return render(request, 'imagelist.html', {'table': table})
        else:
            variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','add_image':add_image})
            return render_to_response('addimage.html',variables )
            
    else:
        add_image= AddForm()
        variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','add_image':add_image})
        return render_to_response('addimage.html',variables )
            

# RegEx to find invalid characters
re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)

def filter_using_re(unicode_string):
    return re_pattern.sub(u'\uFFFD', unicode_string)

def display_feeds(request):
    if request.method == 'POST':
        feedlist = request.POST.get('hdnCheck','0').split(',') 
        feedObjList = FeedItem.objects.filter(pk__in=feedlist) 
        for row in  feedObjList:
            from BeautifulSoup import BeautifulSoup
            import urllib, cStringIO
            from PIL import Image
            soup = BeautifulSoup(row.summary)
            tags=soup.findAll('img')
            s= list(set(tag['src'] for tag in tags))
            for src in s:
                
                fileval = cStringIO.StringIO(urllib.urlopen(src).read())
                im=Image.open(fileval)
                height, width = im.size
                if width>200:
                    print "innnnnnnnnnnnnnnnnnnnnnnnnnn"
                    image = src
                    if request.POST.get('postType','') == "Outposts":
                        i = Outposts(title=row.title,
                                     img=image,
                                     url=row.url,
                                     author=row.author,
                                     color = request.POST.get('color',''),
                                     region = request.POST.get('region',''),
                                     room =request.POST.get('room',''),
                                     style = request.POST.get('style',''),
                                     updatedDate = row.updatedDate)                             
                        i.save()
                    elif request.POST.get('postType','') == "Inspiration":
                        
                        i = Inspiration(title=row.title,
                                     img=image,
                                     url=row.url,
                                     author=row.author,
                                     color = request.POST.get('color',''),
                                     region = request.POST.get('region',''),
                                     room =request.POST.get('room',''),
                                     style = request.POST.get('style',''),
                                     updatedDate = row.updatedDate)                             
                        i.save()
                    elif request.POST.get('postType','') == "Color":
                        i = Colors(title=row.title,
                                     img=image,
                                     url=row.url,
                                     author=row.author,
                                     color = request.POST.get('color',''),
                                     region = request.POST.get('region',''),
                                     room =request.POST.get('room',''),
                                     style = request.POST.get('style',''),
                                     updatedDate = row.updatedDate)                             
                        i.save()
                    elif request.POST.get('postType','') == "Bazaar":
                        i = Bazaar(title=row.title,
                                     img=image,
                                     url=row.url,
                                     author=row.author,
                                     color = request.POST.get('color',''),
                                     region = request.POST.get('region',''),
                                     room =request.POST.get('room',''),
                                     style = request.POST.get('style',''),
                                     updatedDate = row.updatedDate)                             
                        i.save()
                    elif request.POST.get('postType','') == "Design Matters":
                        i = Designs(title=row.title,
                                     img=image,
                                     url=row.url,
                                     author=row.author,
                                     color = request.POST.get('color',''),
                                     region = request.POST.get('region',''),
                                     room =request.POST.get('room',''),
                                     style = request.POST.get('style',''),
                                     updatedDate = row.updatedDate)                             
                        i.save()
                        
                  
    else:        
        pass
                        
    feed_items = FeedItem.objects.all()        
    table = FeedItemTable(feed_items)
    form =VaultForm()
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    return render(request, 'display_feeds.html', {'table': table,'form':form})
    
def fetch_feeds(request):
    feeds = Feed.objects.all()
    print "feeddddddddddd"
    for feed in feeds:
        print "Bye"
        feed_items = feedparser.parse(feed.URL)
        print "feedssssss", feed.URL
        if feed_items['entries'] :
            print "feed_itemsssssss"
            
            for item in feed_items['entries']:   
                    publishedDate = datetime.datetime.strptime(item['updated'][:25], '%a, %d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
                    #Ensure the same item is not repeated             
                    try: 
                        FeedItem.objects.get(url=item['link'],
                                                   publishedDate__lte=publishedDate)
                    except FeedItem.DoesNotExist:          
                        i = FeedItem(title=filter_using_re(item['title']),
                                     summary=filter_using_re(item['summary']),
                                     url=filter_using_re(item['link']),
                                     author=filter_using_re(item['author']),
                                     publishedDate=publishedDate)                             
                        i.save()
                        
    feed_items = FeedItem.objects.all()        
    table = FeedItemTable(feed_items)
    form =VaultForm()
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    return render(request, 'display_feeds.html', {'table': table,'form':form})
                            
                        
    
    
def filterImagesByUrl(request):
    from BeautifulSoup import BeautifulSoup
    import urllib, cStringIO
    from PIL import Image
    feed_items = FeedItem.objects.all() 
    for row in feed_items:
        
        soup = BeautifulSoup(row.summary)
        tags=soup.findAll('img')
        s= list(set(tag['src'] for tag in tags))
        for src in s:
            fileval = cStringIO.StringIO(urllib.urlopen(src).read())
            im=Image.open(fileval)
            height, width = im.size
            i = Imagelist(title='',
                         src=src,
                         height=str(height),
                         width=str(width))
            i.save()
            
    return HttpResponse('success')
