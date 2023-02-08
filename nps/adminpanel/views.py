from django.shortcuts import render, redirect
from django.apps import apps


# Create your views here.
def dashboard(r):
    return render(r,'admin/dashboard.html')
def adminpanel(r):
    patent = apps.get_model('Patent', 'Patentapplication')
    cp = apps.get_model('Copyright','Copyright')
    des = apps.get_model('Design','Design')
    return render(r, "admin/admin.html", {'con': patent.objects.all(),'cp':cp.objects.all(),'des':des.objects.all()})


def Editapplication(r, uid):
    patent = apps.get_model('Patent', 'Patentapplication')
    patent = patent.objects.get(uid=uid)
    nda = apps.get_model('Patent', 'NDAStatus')
    paymentstatus = apps.get_model('Patent', 'PaymentStatus')
    DocumentationStatus = apps.get_model('Patent', 'DocumentationStatus')
    NoveltyStatus = apps.get_model('Patent', 'NoveltyStatus')
    DraftingStatus = apps.get_model('Patent', 'DraftingStatus')
    ExaminationSatus = apps.get_model('Patent', 'ExaminationSatus')
    DrawingStatus = apps.get_model('Patent', 'DrawingStatus')
    FilingStatus = apps.get_model('Patent', 'FilingStatus')
    FerStatus = apps.get_model('Patent', 'FerStatus')
    HearingStatus = apps.get_model('Patent', 'HearingStatus')
    GrantsStatus = apps.get_model('Patent', 'GrantsStatus')
    context = {'app': patent, 'paymentstatus': paymentstatus.objects.filter(uid=uid),
               'ndastatus': nda.objects.get(uid=uid)}
    c = {}
    if patent.patenttype == 'full':
        c = {'GrantsStatus': GrantsStatus.objects.get(uid=uid),
             'DocumentationStatus': DocumentationStatus.objects.get(uid=uid),
             'FerStatus': FerStatus.objects.get(uid=uid), 'NoveltyStatus': NoveltyStatus.objects.get(uid=uid),
             'DraftingStatus': DraftingStatus.objects.get(uid=uid),
             'FilingStatus': FilingStatus.objects.get(uid=uid),
             'DrawingStatus': DrawingStatus.objects.get(uid=uid),
             'HearingStatus': HearingStatus.objects.get(uid=uid),
             'ExaminationStatus': ExaminationSatus.objects.get(uid=uid)}
    elif patent.patenttype == 'novelty search':
        c = {'NoveltyStatus': NoveltyStatus.objects.get(uid=uid)}
    elif patent.patenttype == 'drafting':
        c = {'DraftingStatus': DraftingStatus.objects.get(uid=uid)}
    elif patent.patenttype == 'drawing':
        c = {'DrawingStatus': DrawingStatus.objects.get(uid=uid)}
    elif patent.patenttype == 'documentation':
        c = {'DocumentationStatus': DocumentationStatus.objects.get(uid=uid)}
    elif patent.patenttype == 'filing':
        c = {'FilingStatus': FilingStatus.objects.get(uid=uid)}
    elif patent.patenttype == 'examination':
        c = {'ExaminationSatus': ExaminationSatus.objects.get(uid=uid)}
    elif patent.patenttype == 'FER':
        c = {'FerStatus': FerStatus.objects.get(uid=uid), }
    elif patent.patenttype == 'hearing':
        c = {'HearingStatus': HearingStatus.objects.get(uid=uid)}
    co = {**context, **c}
    return render(r, 'Patent/editappliaction.html', co)


def ndsatatus(r):
    nda = apps.get_model('Patent', 'NDAStatus')
    if r.method == 'POST':
        uid = r.POST['uid']
        status = r.POST['status']
        ndas = nda.objects.get(uid=uid)
        ndas.status = True
        ndas.nda = status
        ndas.save()
        return redirect('user/login')


def filingstatus(r):
    FilingStatus = apps.get_model('Patent', 'FilingStatus')
    if r.method == 'POST':
        uid = r.POST['uid']
        sta = FilingStatus.objects.get(uid=uid)
        sta.status = True
        sta.save()
        return redirect('user/login')

def dashboard(r):
    return redirect('user/login')

def closeapplication(r):
    patent = apps.get_model('Patent', 'Patentapplication')
    if r.method == 'POST':
        uid = r.POST['uid']
        patent = patent.objects.get(uid=uid)
        patent.status = True
        patent.save()
        return redirect('user/login')
def openapplication(r):
    patent = apps.get_model('Patent', 'Patentapplication')
    if r.method == 'POST':
        uid = r.POST['uid']
        patent = patent.objects.get(uid=uid)
        patent.status = False
        patent.save()
        return redirect('user/login')

def EditapplicationCopyright(r,uid):
    cp = apps.get_model('Copyright','Copyright').objects.get(uid=uid)
    return render(r,'Copyright/editapp.html',{'c':cp})

def track(r):
    patent = apps.get_model('Patent', 'Patentapplication')
    cp = apps.get_model('Copyright', 'Copyright')
    des = apps.get_model('Design', 'Design')
    return render(r, "admin/track.html", {'con': patent.objects.all(),'cp':cp.objects.all(),'des':des.objects.all()})