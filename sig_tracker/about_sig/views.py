from . models import Sig
from . models import Topics
from django.shortcuts import render
from django.http import Http404

<<<<<<< HEAD
=======

>>>>>>> upstream/master
def index(request):
    all_sig = Sig.objects.all()
    #context = {'all_sig': all_sig }
    return render(request,'about_sig/index.html',{'all_sig': all_sig})

<<<<<<< HEAD


=======
>>>>>>> upstream/master
def detail(request, sig_id):
    try:
        sig = Sig.objects.get(pk=sig_id)
    except Sig.DoesNotExist:
        raise Http404("SIG does not exist")
    return render(request, 'about_sig/detail.html', {'sig': sig})
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> upstream/master
=======
>>>>>>> 39b819b6744c64ef961942633ec4912bf989ead7
