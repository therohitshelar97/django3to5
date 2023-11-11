"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fetching/',views.Fetch,name="fetching"),
    path('form/',views.Form, name="form"),
    path('update/<int:id>',views.Update, name="update"),
    path('animals/',views.Animals,name='animals'),
    path('static1/',views.Static1),
    path('orm/',views.Orm, name='orm'),
    path('addtocart/', views.add_to_cart,name='addtocart'),
    path('viewcart/',views.view_cart, name="viewcart")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
