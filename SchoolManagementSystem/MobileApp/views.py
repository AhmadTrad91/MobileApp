from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user

from MobileApp.models import *


def index(request):
	return render(request, "index.html", {
		"name": "YOU"
		})