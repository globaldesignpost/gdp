import django_tables2 as tables
from gdp.models import Feed,Upload,FeedItem
from django.utils.safestring import mark_safe
from django.utils.html import escape
class FeedTable(tables.Table):
    class Meta:
        model = Feed
        attrs = {"class": "table table-hover table-bordered table-stripped"}
        
        
        
class UploadTable(tables.Table):
    
    def render_upload(self,value):
        #value  = value.strip('gdp')
        #print value.image.url
        url =  str(value).split('gdp')[1]
        return mark_safe('<a class="thumbnail" href="#"><img src="%s" style="width:100px;height:100px;"/></a>'%escape(url))
    class Meta:
        model = Upload
        attrs = {"class": "table table-hover table-stripped upload_table"}
        
        
class FeedItemTable(tables.Table):
    class Meta:
        model = FeedItem
        attrs = {"class": "table table-hover table-bordered table-stripped"}