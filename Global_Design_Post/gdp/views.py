# Create your views here.
import os
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.shortcuts import redirect
from gdp.forms import RegistrationForm, FeedForm
from gdp.models import Feed
from gdp.forms import RegistrationForm,PasswordReCaptchaForm
def home(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('index.html',variables )


def registerUser(request):
    if request.method == 'POST':
        form = PasswordReCaptchaForm(request.POST)
        if form.is_valid():
            dictParamList = {}
            dictParamList['email'] = form.cleaned_data['email'].strip()
            dictParamList['userName'] = form.cleaned_data['userName'].strip()
            dictParamList['password'] = form.cleaned_data['password'].strip()
            
            #objUserManagementDA = usermanagementDA()
            #objUserManagementDA.createuser(dictParamList)
            #return HttpResponse('success')
            variables = RequestContext(request, {'welcomeMsg':'','formR':form})
            return render_to_response('registration.html',variables )
        else:
            
            variables = RequestContext(request, {'welcomeMsg':'','formR':form})
            return render_to_response('registration.html',variables )
    else:
        form = PasswordReCaptchaForm()
        variables = RequestContext(request, {'welcomeMsg':'','form':form})
        return render_to_response('registration/login.html',variables )
        return HttpResponseRedirect('s') 

def favorites(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('favourite.html',variables )

def bazaar(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('bazaar.html',variables )

def mygdp(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('mygdp.html',variables )

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
    add_feed= FeedForm()
    list_feed = Feed.objects.all()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.',
                                         'error_header':'Error!',
                                         'add_feed': add_feed,
                                         'list_feed': list_feed})
    return render_to_response('feed.html',variables )