"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from apps_module.membership.views import member_data, save_membership_data, attendance_data, save_attendance_data

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),

    path('member_data', member_data),
    path('save_membership_data', save_membership_data),
    path('attendance_data', attendance_data),
    path('save_attendance_data', save_attendance_data)



]

admin.site.site_header = 'G.E.C Mt. Zion Administration'
