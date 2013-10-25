import django_tables2 as tables
from gdp.models import Feed

class FeedTable(tables.Table):
    class Meta:
        model = Feed
        attrs = {"class": "table table-hover table-bordered table-stripped"}