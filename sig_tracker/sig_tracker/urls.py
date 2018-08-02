from django.contrib import admin
from django.conf.urls import include,url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d877ca33a0e342146d320beb8f51ec8ba8d08f89
    url(r'^main/', include('main.urls')),
]


<<<<<<< HEAD
=======
    url(r'^about_sig/', include('about_sig.urls')),
]
>>>>>>> cf5cbc2b5711cbff71253c61e37f596c59b7bfac
=======
>>>>>>> d877ca33a0e342146d320beb8f51ec8ba8d08f89
