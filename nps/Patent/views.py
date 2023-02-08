import random

from django.apps import apps
from django.shortcuts import render, redirect
from .models import Patentapplication, NDAStatus, PaymentStatus, NoveltyStatus, DocumentationStatus, DrawingStatus, \
    DraftingStatus, FerStatus, ExaminationSatus, FilingStatus, HearingStatus, GrantsStatus


def random_string(ReferedBy):
    unique_id = ReferedBy[0:2] + "".join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    return unique_id


# Create your views here.
def FullPatentapplicationview(request):
    referedby = apps.get_model('login', 'referdby')
    if request.method == 'POST':
        title = request.POST['title']
        organization = request.POST['organization']
        modeofcontact = request.POST['modeofcontact']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        uid = random_string(referedby)
        date = request.POST['date']

        r = Patentapplication(title=title, uid=uid, organisation=organization, referedby=referedby
                              , conntactnumber=contactnumber, emailid=emailid, modeofcontact=modeofcontact,
                              patenttype='full', status=False,date=date)
        r.save()
        NDAStatus(uid=uid, status=False).save()
        NoveltyStatus(uid=uid, status=False).save()
        DraftingStatus(uid=uid, status=False).save()
        DrawingStatus(uid=uid, status=False).save()
        DocumentationStatus(uid=uid, status=False).save()
        FilingStatus(uid=uid, status=False).save()
        ExaminationSatus(uid=uid, status=False).save()
        FerStatus(uid=uid, status=False).save()
        HearingStatus(uid=uid, status=False).save()
        GrantsStatus(uid=uid, status=False).save()
        PaymentStatus(uid=uid, status=False).save()
        return redirect('home')
    return render(request, "Patent/FullPatentapplication.html",{'ref':referedby.objects.all})


def Patentapplicationview(request):
    referedby = apps.get_model('login', 'referdby')
    if request.method == 'POST':
        title = request.POST['title']
        type = request.POST['check[]']
        organization = request.POST['organization']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        modeofcontact = request.POST['modeofcontact']
        uid = random_string(referedby)
        date = request.POST['date']
        r = Patentapplication(uid=uid, title=title, organisation=organization, referedby=referedby
                              , conntactnumber=contactnumber, emailid=emailid, modeofcontact=modeofcontact,date=date,
                              patenttype=type)
        r.save()
        NDAStatus(uid=uid, status=False).save()
        if type == 'novelty search':
            NoveltyStatus(uid=uid, status=False).save()
        if type == 'drafting':
            DraftingStatus(uid=uid, status=False).save()
        if type == 'drawing':
            DrawingStatus(uid=uid, status=False).save()
        if type == 'documentation':
            DocumentationStatus(uid=uid, status=False).save()
        if type == 'filing':
            FilingStatus(uid=uid, status=False).save()
        if type == 'examination':
            ExaminationSatus(uid=uid, status=False).save()
        if type == 'FER':
            FerStatus(uid=uid, status=False).save()
        if type == 'hearing':
            HearingStatus(uid=uid, status=False).save()
        GrantsStatus(uid=uid, status=False).save()
        PaymentStatus(uid=uid, status=False).save()
        return redirect('home')
    else:
        return render(request, "Patent/Patentapplication.html",{'ref':referedby.objects.all})


def Documentationstatusview(r, uid):
    documentationstatus=Patentapplication.objects.get(uid=uid,patenttype='documentation')

    return render(r, "Patent/Documentationstatus.html",{'c':documentationstatus})


def Documentationtableview(r):
    return render(r, "Patent/Documentationtable.html")


def Draftingstatusview(r, uid):
    draftingstatus = Patentapplication.objects.get(uid=uid)
    return render(r, "Patent/Draftingstatus.html",{'c':draftingstatus})


def Draftingtableview(r):
    return render(r, "Patent/Draftingtable.html")


def Drawingstatusview(r, uid):
    drawingstatus=Patentapplication.objects.get(uid=uid)
    return render(r, "Patent/Drawingstatus.html",{'c':drawingstatus})


def Drawingtableview(r):
    return render(r, "Patent/Drawingtable.html")


def Patentabilitysearchstatusview(r, uid):
    patentabilitysearchstatus=Patentapplication.objects.get(uid=uid)
    return render(r, "Patent/Patentabilitysearchstatus.html",{'c':patentabilitysearchstatus})


def Patentabilitysearchtableview(r):
    return render(r, "Patent/Patentabilitysearchtable.html")

def Drawingstatusdata(r):
    if r.method=='POST':
        uid=r.POST['uid']
        r=DrawingStatus.objects.get(uid=uid)
        r.status=True
        r.save()
        return redirect('user/login')

def Documentationstatusdata(r):
    if r.method=='POST':
        uid=r.POST['uid']
        r=DocumentationStatus.objects.get(uid=uid)
        r.status=True
        r.save()
    return redirect('user/login')
def Draftingstatusdata(r):
    if r.method=='POST':
        uid=r.POST['uid']
        r=DraftingStatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')
def GrantsStatusdata(r):
    if r.method=='POST':
        uid=r.POST['uid']
        r=GrantsStatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')
def FilingStatusdata(r):
    if r.method=='POST':
        uid=r.POST['uid']
        r=FilingStatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')
def ExaminationSatusdata(r):
    if r.method=='POST':
        uid=r.POST['uid']
        r=ExaminationSatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')
def FerStatusdata(r):
    if r.method=='POST':
        uid=r.POST['uid']
        r=FerStatus.objects.get(uid=uid)
        r.status = True
        r.save()
    return redirect('user/login')

def Patentabilitysearchstatusdata(r):
        if r.method == "POST":
            uid = r.POST['uid']
            n = NoveltyStatus.objects.get(uid = uid)
            n.status = True
            n.save()
            return redirect('user/login')

        return redirect('user/login')
def Hearingstatusdata(r):
        if r.method == "POST":
            uid = r.POST['uid']
            date = r.POST['date']
            n = HearingStatus.objects.get(uid = uid)
            n.status = True
            n.date=date
            n.save()
            return redirect('user/login')

        return redirect('user/login')
def paymentStatus(r):
    if r.method=='POST':
        uid=r.POST['uid']
        amount = r.POST['amount']
        p = PaymentStatus.objects.get(uid=uid)
        p.status = True
        p.amount = amount
        p.save()
    return redirect('user/login')
