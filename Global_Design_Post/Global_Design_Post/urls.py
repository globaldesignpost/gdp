from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gdp.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$',"gdp.views.logout"),
    url(r'^register/$','gdp.views.registerUser' ),
    url(r'^requestPassword/$','gdp.views.requestPassword'),
    url(r'^resetPassword/(.*)/','gdp.views.resetPassword'),
    url(r'^favorites/$', 'gdp.views.favorites', name='favorites'),
    url(r'^bazaar/$', 'gdp.views.bazaar', name='bazaar'),
    url(r'^mygdp/$', 'gdp.views.mygdp', name='mygdp'),
    url(r'^feed/$', 'gdp.views.feed', name='feed'),
    url(r'^myProfile/$', 'gdp.views.myProfile', name='feed'),
    url(r'^outposts/$', 'gdp.views.outposts', name='outposts'),
    url(r'^inspiration/$', 'gdp.views.inspiration', name='inspiration'),
    url(r'^colors/$', 'gdp.views.colors', name='colors'),
    url(r'^addimage/$', 'gdp.views.addimage', name='addimage'),
    url(r'^imagelist/$', 'gdp.views.imagelist', name='addimage'),
    url(r'^display_feeds/$', 'gdp.views.display_feeds', name='display_feeds'),
    #url(r'^requestPassword/$','gdp.views.requestPassword'),
    #url(r'^resetPassword/(.*)/','gdp.views.resetPassword'),
    url(r'^filterImagesByUrl/$', 'gdp.views.filterImagesByUrl', name='filterImagesByUrl'),
    url(r'^vault/$', 'gdp.views.vault', name='vault'),
    url(r'^fetch_feeds/$', 'gdp.views.fetch_feeds', name='fetch_feeds'),
    url(r'^feed_delete/$', 'gdp.views.feed_delete', name='feed_delete'),
    
    
    # url(r'^Global_Design_Post/', include('Global_Design_Post.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
     
)
#include('password_reset.urls')