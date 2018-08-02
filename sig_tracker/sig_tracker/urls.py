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
>>>>>>> cf5cbc2b5711cbff71253c61e37f596c59b7bfac
