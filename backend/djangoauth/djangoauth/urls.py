# """djangoauth URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    # re_path(r'^(?:.*)/?$',TemplateView.as_view(template_name="index.html"), name="home"),
    # Django Admin, use {% url 'admin:index' %}
    path('admin/', admin.site.urls),

    # LandingPage_API Application
    # path('api/', include('blog.api.urls', namespace='blog_api')),
]


# API URLS
urlpatterns += [
    # API User Register url
    path('api/user/', include('authentication.urls')),
    # DRF JWT auth token url
    path('api/token/', include('authentication.api.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
