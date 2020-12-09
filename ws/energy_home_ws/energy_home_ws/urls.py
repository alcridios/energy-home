"""energy_home_ws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from energy_home_ws.views import client, client_by_id, contact_information, contact_information_by_id, add_client,delete_client
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/client/', client, name='client'),
    path('api/v1/client/<int:id>/', client_by_id, name='client-by-id'),
    path('api/v1/contact-information/', contact_information, name='contact-information'),
    path('api/v1/contact-information/<int:id>/', contact_information_by_id, name='contact-information-by-id'),
    path('api/v1/add-client/', add_client, name='add-client'),  
    path('api/v1/del-client', delete_client, name='del-client'),  

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

