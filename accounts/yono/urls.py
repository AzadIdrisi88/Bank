from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bank/',views.bank),
    path('',views.display),
    path('details/',views.details),
    path('deposite/',views.deposite),
    path('withdraw/',views.withdraw),
    
]
