
from django.urls import path
from pinterest import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.home, name="Home"),
    path('explorar', views.explorar, name="explorar"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)