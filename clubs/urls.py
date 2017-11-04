from django.conf.urls import url
from .views import ClubList

urlpatterns=[
    url(r'^$', ClubList.as_view(), name="clublist"),
]