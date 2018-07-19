from django.conf.urls import url
from . import views


app_name = 'dev_sig'
urlpatterns = [
    #/dev_sig/
    url(r'^', views.index, name='index'),
    #/dev_sig/1/
<<<<<<< HEAD
    url(r'^(?P<sig_id>[0-9]+)/$', views.detail, name='detail'),
=======
    url(r'(?P<sig_id>[0-9]+)/$', views.detail, name='detail'),
>>>>>>> 39b819b6744c64ef961942633ec4912bf989ead7
]
