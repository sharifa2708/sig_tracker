<<<<<<< HEAD
from . models import Sig, DevSig
from django.shortcuts import render
from django.http import Http404

from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class index(TemplateView):
    template_name = "index.html"

class dev_sig(TemplateView):
    template_name = "dev_sig.html"

class ml_sig(TemplateView):
    template_name = "ml_sig.html"

class cp_sig(TemplateView):
    template_name = "cp_sig.html"
=======
from . models import Sig
from . models import Topics
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_sig = Sig.objects.all()
    #context = {'all_sig': all_sig }
    return render(request,'main/index.html',{'all_sig': all_sig})

def detail(request, sig_id):
    try:
        sig = Sig.objects.get(pk=sig_id)
    except Sig.DoesNotExist:
        raise Http404("SIG does not exist")
    return render(request, 'main/detail.html', {'sig': sig})
>>>>>>> d877ca33a0e342146d320beb8f51ec8ba8d08f89
