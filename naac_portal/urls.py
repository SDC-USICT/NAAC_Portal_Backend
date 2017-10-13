"""naac_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from employee.views import *
from patents.views import patent
from awards.views import award
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/school', school_details),
    url(r'^api/login', login),
    url(r'^api/awards', awards),
    url(r'^api/$', employee),
    url(r'^api/extra', extra),
    url(r'^api/guest', guest),
    url(r'^api/membership', moab),
    url(r'^api/columns', columns),
    url(r'^api/get', get_data),
    url(r'^api/post', post_data),
    url(r'^api/employee',employee_details),
    url(r'^api/emppost',update_emp_details),
    url(r'^api/upload',imageUpload),
    url(r'^api/delete', delete_data),
    url(r'^api/verify_coauthor', verify_coauthor),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)