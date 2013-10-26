# Create your views here.
import os
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.shortcuts import redirect
from gdp.forms import RegistrationForm, FeedForm ,MyProfileForm,AddForm
from gdp.models import Feed
from gdp.forms import RegistrationForm,PasswordReCaptchaForm
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate,login
from django.contrib import auth
from gdp.tables import FeedTable
from django.shortcuts import render
from django_tables2  import RequestConfig
def home(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
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
            dictParamList['password'] = form.cleaned_data['password'].strip()
            
            return HttpResponse('success')
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
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('colors.html',variables )

def myProfile(request):
    form =MyProfileForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','form':form})
    return render_to_response('myProfile.html',variables )

def bazaar(request):
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('bazaar.html',variables )

@login_required
def mygdp(request):
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('mygdp.html',variables )

def outposts(request):
    form =MyProfileForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','form':form})
    return render_to_response('outposts.html',variables )

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
    
    
def addimage(request):
    if request.method == 'POST':
        add_image = AddForm(request.POST)
        if add_image.is_valid():
            add_image.save()
            return HttpResponseRedirect('/imagelist/')
        else:
            variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','add_image':add_image})
            return render_to_response('addimage.html',variables )
            
    else:
        add_image= AddForm()
        variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!','add_image':add_image})
        return render_to_response('addimage.html',variables )
            
