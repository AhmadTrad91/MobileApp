from django.conf.urls import url

from MobileApp import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
]
