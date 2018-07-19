from django.contrib import admin
from django.conf.urls import include,url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^main/', include('main.urls')),
]
=======
    url(r'^about_sig/', include('about_sig.urls')),
]
>>>>>>> bc743e6ad624fa4dc5c5ab6f9c56f3f6b5795605
