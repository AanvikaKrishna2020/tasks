
from django.urls import path

from tasksapp import views

urlpatterns = [

    # path('',views.home,name='home'),
    # path('over',views.over,name='over'),
    # path('contact',views.contact,name='contact'),
    # path('details',views.details,name='details'),
    # path('thanks',views.thanks,name='thanks')
    path('',views.result,name='result'),
    path('add/',views.results,name='results')
]
