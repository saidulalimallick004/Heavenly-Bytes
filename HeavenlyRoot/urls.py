"""
URL configuration for HeavenlyRoot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

from .views import *
from Home.views import *
from Users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #--------------------------------------------------------------------------
        # Home ---->>
    
    path("",homePage,name='Heavenly-Bytes'),
    path("home/",homePage,name='Heavenly-Bytes'),
    path("explore/",explorePage,name='Heavenly-Bytes-Explore'),
    path("aboutus/",aboutUsPage,name='Heavenly-Bytes-AboutUs'),
    path("contactus/",contactUsPage,name='Heavenly-Bytes-ContactUs'),
    
    
    #--------------------------------------------------------------------------
        # Users ---->>
    
    path("createaccount/",createAccount,name="Create Account"),
    path("login/",loginAccount,name="Login"),
    path("logout/",logoutAccount,name="Logout"),
    path("profile/",userProfile,name='Profile'),
    path("dashboard/",userDashboard,name='Dashboard'),
    path("verifyemail/",verifyEmail,name='Email-Verify'),
    path("otpconformation/",otpConformation,name='Email-OTP'),
    
    
    #--------------------------------------------------------------------------
        # Orders ---->>
    
    path("order/",include("Orders.urls")),
    
    #--------------------------------------------------------------------------
        # Blog ---->>
    
    path("blog/",include("Blog.urls")),
    
    #--------------------------------------------------------------------------
        # Menus ---->>
    
    path("menus/",include("Menus.urls")),
    
    #--------------------------------------------------------------------------
        # Inventory ---->>
    
    path("inventory/",include("Inventory.urls")),

    #--------------------------------------------------------------------------
        # Notifications ---->>
    
    path("notifications/",include("Notifications.urls")),
    
    #--------------------------------------------------------------------------
        # Payments ---->>
    
    path("payments/",include("Payments.urls")),
    
    #--------------------------------------------------------------------------
        # Reservations ---->>
    
    path("reservations/",include("Reservations.urls")),
    
    #--------------------------------------------------------------------------
        # Reviews ---->>
    
    path("reviews/",include("Reviews.urls")),
        
]




handler404=custom_404