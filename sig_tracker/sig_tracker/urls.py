<<<<<<< HEAD

=======
>>>>>>> upstream/master
from django.contrib import admin
from django.conf.urls import include,url

urlpatterns = [
<<<<<<< HEAD
    url(r'admin/', admin.site.urls),
    url(r'about_sig/', include('about_sig.urls')),
=======
    url(r'^admin/', admin.site.urls),
    url(r'^about_sig/', include('about_sig.urls')),
>>>>>>> upstream/master
]
