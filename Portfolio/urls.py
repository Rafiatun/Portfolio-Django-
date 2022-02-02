
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('rafia556admin/', admin.site.urls),
    path('',include('Main.urls'))
]
