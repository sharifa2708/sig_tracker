from django.conf.urls import url
from . import views

app_name = 'about_sig'
urlpatterns = [
    #/about_sig/
<<<<<<< HEAD
    url(r'', views.index, name='index'),
    #/about_sig/1/
    url(r'(?P<sig_id>[0-9]+)/$', views.detail, name='detail'),
<<<<<<< HEAD


]
=======
    url(r'^', views.index, name='index'),
    #/about_sig/1/
    url(r'^(?P<sig_id>[0-9]+)/$', views.detail, name='detail'),
]
>>>>>>> upstream/master
=======
]
>>>>>>> 39b819b6744c64ef961942633ec4912bf989ead7
