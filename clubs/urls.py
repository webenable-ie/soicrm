from django.conf.urls import url
from .views import ClubListView, ClubDetailsView

urlpatterns=[
    url(r'^$', ClubListView.as_view(), name="club_list"),
    url(r'^(?P<slug>[-\w]+)/$', ClubDetailsView.as_view(), name="club_details")
]