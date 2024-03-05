from django.urls import path
from . import views
urlpatterns=[
    path("index/",views.main,name="index"),
    path("home/",views.home,name='home'),
    path("rooms/",views.rooms,name='rooms'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),
    path("demo/",views.demo,name="demo"),
    path("result/",views.result,name="result"),
    path("demo1/",views.demo1,name="demo1"),
    path("result1/",views.result1,name="result1"),
    path("d/",views.d,name="d"),
    path("r/",views.r,name="r"),
    path("cake/",views.cakess,name="cake"),
    path("detail/<id>",views.detail,name='detail'),
    path("car/",views.car,name='car'),
    path("maclloc",views.maclloc,name="maclloc")
]
