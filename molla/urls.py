"""
URL configuration for molla project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from front_end.views import *
from admin_side.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('login/',user_login),
    path('logout/',user_logout),
    path('about/',about),
    path('shop/',shop),
    path('cart/',cart_ft),
    path('checkout/',checkout),
    path('wishlist/',wishlist),
    path('faq/',faq),
    path('category/',category_all),
    path('single_product/',single_product),
    path('dashboard/',dashboard),
    path('signup/',registration),
    path('add_cart/<int:cart_id>',add_cart),
    path('add_wishlist/<int:wish_id>',add_wishlist),
    path('myadmin/dashboard/',admin_dashboard),
    path('myadmin/signin/',admin_signin),
    path('myadmin/signup/',admin_signup),
    path('myadmin/logout/',admin_logout),
    path('myadmin/add_slide/',add_slide),
    path('myadmin/manage_slide/',manage_slide),
    path('myadmin/update_slide/<int:edit>',update_slide),
    path('myadmin/delete_slide/<int:delt>',delete_slide),
    path('myadmin/add_brand/',add_brand),
    path('myadmin/manage_brand/',manage_brand),
    path('myadmin/update_brand/<int:edit>',update_brand),
    path('myadmin/delete_brand/<int:delt>',delete_brand),
    path('myadmin/add_category/',add_category),
    path('myadmin/manage_category/',manage_category),
    path('myadmin/update_category/<int:edit>',update_category),
    path('myadmin/delete_category/<int:delt>',delete_category),
    path('myadmin/add_subcategory/',add_subcategory),
    path('myadmin/manage_subcategory/',manage_subcategory),
    path('myadmin/update_subcategory/<int:edit>',update_subcategory),
    path('myadmin/delete_subcategory/<int:delt>',delete_subcategory),
    path('myadmin/add_product/',add_product),
    path('myadmin/manage_product/',manage_product),
    path('myadmin/update_product/<int:edit>',update_product),
    path('myadmin/delete_product/<int:delt>',delete_product),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
