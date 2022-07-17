from django.urls import path
from . import views


app_name = "link"

urlpatterns = [
    path("active/", ActiveLinkView.as_view(), name='active_link'),
    path("recent/", RecentLinkView.as_view(), name='recent_link'),


]

