from django.contrib import admin
from . models import Sig
<<<<<<< HEAD
from . models import DevSig
from . models import MlSig
from . models import CpSig

admin.site.register(Sig)
admin.site.register(DevSig)
admin.site.register(MlSig)
admin.site.register(CpSig)
=======
from . models import Topics

admin.site.register(Sig)
admin.site.register(Topics)
>>>>>>> d877ca33a0e342146d320beb8f51ec8ba8d08f89
