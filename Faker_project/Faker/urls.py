from os import name
from django.urls import path
from .views import Paginationshowview, Populate



urlpatterns=[
    path('pol/',Populate,name='populate'),
    path('pagination/',Paginationshowview,name='pagination')
]