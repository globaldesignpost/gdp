from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from gdp.views import *
urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'Global_Deisgn_post.gdp.views.home', name='home'),
     url(r'^favorites/$', 'Global_Deisgn_post.gdp.views.favorites', name='favorites'),
     url(r'^bazaar/$', 'Global_Deisgn_post.gdp.views.bazaar', name='bazaar'),
     url(r'^mygdp/$', 'Global_Deisgn_post.gdp.views.mygdp', name='mygdp'),
     url(r'^unzip/(\w*)', 'Global_Deisgn_post.gdp.views.unzip', name='favorites'),
     #url(r'^Global_Deisgn_post/', include('Global_Deisgn_post.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
