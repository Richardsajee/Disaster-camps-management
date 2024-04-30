import random
import smtplib
from _datetime import datetime
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.db.models.expressions import RawSQL
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.

projectpath = r"C:\Users\richa\OneDrive\Desktop\Camp\camp\camp\myapp\static\files\\"


def default(request):
    return render(request, 'index.html')


def login_post(request):
    un = request.POST['textfield']
    pas = request.POST['textfield2']
    res = login.objects.filter(username=un, password=pas)
    if res.exists():
        request.session['lid'] = res[0].id
        if res[0].usertype == 'admin':
            request.session['lg'] = 'lin'
            return HttpResponse('<script>alert("Login");window.location="/admin_index"</script>')
        elif res[0].usertype == 'subadmin':
            request.session['subadminid'] = subadmin.objects.get(LOGIN=res[0].id).id
            request.session['lg'] = 'lin'
            return HttpResponse('<script>alert("Login");window.location="/sa_admin_index"</script>')
        elif res[0].usertype == 'volunteer':

            if campallocation.objects.filter(Volunteer__Login=res[0], status="approved"):
                request.session['lg'] = 'lin'
                request.session['vid'] = volunteer.objects.get(Login=res[0].id).id
                return HttpResponse('<script>alert("Login");window.location="/vol_index"</script>')
            else:
                return HttpResponse('<script>alert("Approve Requests First");window.location="/volunteer_unapproved"</script>')
        else:
            return HttpResponse('<script>alert("Missmatch");window.location="/"</script>')
    else:
        return HttpResponse('<script>alert("Not found");window.location="/"</script>')


def volunteer_unapproved(request):
    print(request.session['lid'])
    obj = campallocation.objects.filter(Volunteer__Login=request.session['lid'], status="pending")
    print(obj)
    return render(request, 'VOLUNTEER/unapprovedindex.html', {"data": obj})


def approve_request(request, id):
    campallocation.objects.filter(id=id).update(status="approved")
    request.session['lg'] = 'lin'
    return redirect('/vol_index')


def reject_request(request, id):
    campallocation.objects.filter(id=id).update(status="rejected")
    return redirect('/volunteer_unapproved')


def admin_index(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'admin/index.html')


def sa_admin_index(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'subadmin/index.html')


def vol_index(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'volunteer/index.html')


def admin_alert_add(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    return render(request, 'admin/alertadd.html')


def alertadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    al = request.POST['textfield']
    lat = request.POST['textfield2']
    lon = request.POST['textfield3']
    obj = alert()
    obj.alert = al
    obj.alert_date = datetime.now().date()
    obj.latitude = lat
    obj.longitude = lon
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/alert_view#login"</script>')


def alert_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = alert.objects.all()
    return render(request, 'admin/alertview.html', {"data": obj})


def admin_alert_edit(request, alertid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = alert.objects.get(id=alertid)
    return render(request, 'admin/alertedit.html', {"data": obj})


def alertedit_post(request, alertid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    lat = request.POST['textfield2']
    lon = request.POST['textfield3']
    al = request.POST['textfield']
    alert.objects.filter(id=alertid).update(alert=al, latitude=lat, longitude=lon)
    return HttpResponse('<script>alert("added");window.location="/alert_view#login"</script>')


def admin_alert_dlt(request, alertid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    alert.objects.filter(id=alertid).delete()
    return HttpResponse('<script>alert("Deleted");window.location="/alert_view#login"</script>')


def admin_camp_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = campallocation.objects.all()
    return render(request, 'admin/campview.html', {"data": obj})


def admin_don_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = donation.objects.all()
    return render(request, 'admin/donview.html', {"data": obj})


def admin_msg_add(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'admin/mssgadd.html')


def msgadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    msg = request.POST['textfield']
    obj = adminmessage()
    obj.message = msg
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/admin_msg_add#login"</script>')


def admin_msg_edit(request, mid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    res = adminmessage.objects.get(id=mid)
    return render(request, 'admin/mssgedit.html', {"data": res})


def msgedit_post(request, mid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    msg = request.POST['textfield']
    adminmessage.objects.filter(id=mid).update(message=msg)
    return HttpResponse("ok")


def admin_msg_dlt(request, mid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    adminmessage.objects.filter(id=mid).delete()
    return HttpResponse('<script>alert("Deleted");window.location="/admin_msg_view#login"</script>')


def admin_msg_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = adminmessage.objects.all()
    return render(request, 'admin/mssgview.html', {"data": obj})


def admin_prc_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = precaution.objects.all()
    return render(request, 'admin/prcview.html', {"data": obj})


def admin_prc_edit(request, pid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = precaution.objects.get(id=pid)
    return render(request, 'admin/precationedit.html', {"data": obj})


def prcedit_post(request, pid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    desp = request.POST['textfield']
    if 'fileField' in request.FILES:
        file = request.FILES['fileField']
        fs = FileSystemStorage()
        date = datetime.now().strftime("%y%m%d-%H%M%S")
        fs.save(projectpath + date + '.mp4', file)
        path = "/static/files/" + date + '.mp4'
        precaution.objects.filter(id=pid).update(description=desp, file=path)
    precaution.objects.filter(id=pid).update(description=desp)
    return HttpResponse('<script>alert("added");window.location="/admin_prc_view#login"</script>')


def admin_prc_dlt(request, pid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    precaution.objects.filter(id=pid).delete()
    return HttpResponse('<script>alert("Deleted");window.location="/admin_prc_view#login"</script>')


def admin_prc_addd(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    return render(request, 'admin/precautionadd,html.html')


def prcaadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    desp = request.POST['textfield']
    file = request.FILES['fileField']
    fs = FileSystemStorage()
    date = datetime.now().strftime("%y%m%d-%H%M%S")
    fs.save(projectpath + date + '.mp4', file)
    path = "/static/files/" + date + '.mp4'
    obj = precaution()
    obj.description = desp
    obj.file = path
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/admin_prc_view#login"</script>')


def admin_subadmin_add(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'admin/subadmin add.html')


def subadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    name = request.POST['textfield']
    email = request.POST['textfield2']
    phno = request.POST['textfield3']
    plc = request.POST['textfield4']
    p = random.randint(0000, 9999)
    if login.objects.filter(username=email).exists():
        return HttpResponse(
            '<script>alert("Email already exists");window.location="/admin_subadmin_view#login"</script>')
    obj2 = login()
    obj2.username = email
    obj2.password = p
    obj2.usertype = 'subadmin'
    obj2.save()
    obj = subadmin()
    obj.name = name
    obj.email = email
    obj.phone = phno
    obj.place = plc
    obj.LOGIN = obj2
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/admin_subadmin_view#login"</script>')


def admin_subadmin_edit(request, subid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = subadmin.objects.get(id=subid)
    return render(request, 'admin/subadmin edit.html', {"data": obj})


def subedit_post(request, subid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    name = request.POST['textfield']
    email = request.POST['textfield2']
    phno = request.POST['textfield3']
    pl = request.POST['textfield4']
    subadmin.objects.filter(id=subid).update(name=name, email=email, phone=phno, place=pl)

    return HttpResponse('<script>alert("added");window.location="/admin_subadmin_view#login"</script>')


def admin_subadmin_dlt(request, subid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    subadmin.objects.filter(id=subid).delete()
    return HttpResponse('<script>alert("Deleted");window.location="/admin_subadmin_view#login"</script>')


def admin_subadmin_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = subadmin.objects.all()
    return render(request, 'admin/subadmin view.html', {"data": obj})


def admin_vol_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = volunteer.objects.all()
    return render(request, 'admin/volunterview.html', {"data": obj})


def admin_whether_add(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    return render(request, 'admin/whetheradd.html')


def whetheradd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    city = request.POST['textfield']
    we = request.POST['textfield2']
    t = request.POST['textfield3']
    h = request.POST['textfield4']
    p = request.POST['textfield5']
    des = request.POST['textfield6']
    obj = whether()
    obj.city = city
    obj.weather = we
    obj.temp = t
    obj.description = des
    obj.humidity = h
    obj.pressure = p
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/admin_whether_add"</script>')


def admin_whether_edit(request, whetherid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = whether.objects.get(id=whetherid)
    return render(request, 'admin/whetheredit.html', {"data": obj})


def whetheredit_post(request, whetherid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    city = request.POST['textfield']
    we = request.POST['textfield2']
    t = request.POST['textfield3']
    h = request.POST['textfield4']
    p = request.POST['textfield5']
    des = request.POST['textfield6']
    obj = whether(id=whetherid)
    obj.city = city
    obj.weather = we
    obj.temp = t
    obj.description = des
    obj.humidity = h
    obj.pressure = p
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/admin_whether_view#login"</script>')


def admin_whether_dlt(request, whetherid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    whether.objects.filter(id=whetherid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/admin_whether_view"</script>')


def admin_whether_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = whether.objects.all()
    return render(request, 'admin/whetherview.html', {"data": obj})


def admin_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    return render(request, 'admin/home.html')


def logout(request):
    request.session['lg'] = ""
    return redirect('/')


# ======================================================================================================================

def subadmin_whether_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = whether.objects.filter(date__icontains=datetime.now().date())
    return render(request, 'subadmin/whetherview.html', {"data": obj})


def sa_campadd(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'subadmin/campadd.html')


def campadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    print(request.POST)

    campname = request.POST['textfield']
    Latitude = request.POST['textfield2']
    Longitude = request.POST['textfield3']

    obj = camp()
    obj.name = campname
    obj.latitude = Latitude
    obj.longitude = Longitude
    obj.SUBADMIN_id = request.session['subadminid']
    obj.save()

    return HttpResponse('<script>alert("added");window.location="/subadmin_campview#login"</script>')


def sa_campedit(request, campid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = camp.objects.get(id=campid)

    return render(request, 'subadmin/campedit.html', {"data": obj})


def campedit_post(request, campid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    campname = request.POST['textfield2']
    Latitude = request.POST['textfield3']
    Longitude = request.POST['textfield4']
    camp.objects.filter(id=campid).update(name=campname, latitude=Latitude, longitude=Longitude)
    return HttpResponse('<script>alert("added");window.location="/subadmin_campview#login"</script>')


def sa_campdlt(request, campid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    camp.objects.filter(id=campid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/subadmin_campview#login"</script>')


def subadmin_campview(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = camp.objects.filter(SUBADMIN=request.session['subadminid'])
    return render(request, 'subadmin/campview.html', {"data": obj})


def sa_admin_msg_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = adminmessage.objects.all()
    return render(request, 'subadmin/msg.html', {"data": obj})


def sa_voladd(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    return render(request, 'subadmin/voladd.html')



def voladd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    p = random.randint(0000, 9999)

    if login.objects.filter(username=email).exists():
        return HttpResponse(
            '<script>alert("Email already exists");window.location="/sa_voladd#login"</script>')

    obj1 = login()
    obj1.username = email
    obj1.password = p
    obj1.usertype = 'volunteer'
    obj1.save()

    obj = volunteer()
    obj.name = name
    obj.email = email
    obj.phone = phone
    obj.Login = obj1
    obj.SUBADMIN_id = request.session['subadminid']
    obj.save()

    gmail = smtplib.SMTP('smtp.gmail.com', 587)

    gmail.ehlo()

    gmail.starttls()

    gmail.login('camp98504@gmail.com', 'vlln hvsa teen dvbo')



    msg = MIMEText("Your Password for yor account is: " + str(p))

    msg['Subject'] = 'Your Account have been created Successfully'

    msg['To'] = email

    msg['From'] = 'camp98504@gmail.com'

    try:

        gmail.send_message(msg)
        print("Success")

    except Exception as e:

        print("COULDN'T SEND EMAIL", str(e))



    return HttpResponse('<script>alert("added");window.location="/sa_voladd"</script>')


def sub_volunteer_allocation(request):

    lii = []
    li = []
    res = campallocation.objects.filter(CAMP__SUBADMIN__LOGIN=request.session['lid'])
    for i in res:
        lii.append(i.CAMP_id)
    print(lii)
    c = camp.objects.filter(SUBADMIN__LOGIN=request.session['lid']).exclude(id__in=lii)

    res = campallocation.objects.filter(CAMP__SUBADMIN__LOGIN=request.session['lid'])
    for i in res:
        li.append(i.Volunteer_id)
    print(li)
    obj = volunteer.objects.filter(SUBADMIN__LOGIN=request.session['lid']).exclude(id__in=li)
    print(obj)
    print(c)


    return render(request, 'subadmin/volunteer allocation.html', {"camp": c, "volunteer":obj})


def sub_volunteer_allocation_post(request):
    campid = request.POST['c']
    volunteerid = request.POST['v']

    obj = campallocation()
    obj.CAMP_id=campid
    obj.Volunteer_id =volunteerid
    obj.status = "pending"
    obj.save()
    return HttpResponse('<script>alert("Allocated"); location="/sub_volunteer_allocation"</script>')


def subadmin_view_allocation_status(request):
    obj = campallocation.objects.filter(CAMP__SUBADMIN__LOGIN=request.session['lid'])
    return render(request, 'subadmin/allocation_status.html', {"data": obj})




def subadmin_volview(request, campid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = campallocation.objects.filter(CAMP=campid)
    request.session['campid'] =campid
    return render(request, 'subadmin/volunterview.html', {"data": obj})


def sub_vol_dlt(request, campid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    volunteer.objects.filter(id=campid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/subadmin_volview/'+str(request.session['campid'])+'#login"</script>')


def sa_msgadd(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'subadmin/mssgadd.html')


def sa_msgadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    message = request.POST['textfield']
    obj = subemergency()
    obj.message = message
    obj.SUBADMIN_id = request.session['subadminid']
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/subadmin_msgaddview#login"</script>')


def subadmin_msgaddview(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = subemergency.objects.filter(SUBADMIN=request.session['subadminid'])
    return render(request, 'subadmin/mssgview.html', {"data": obj})


def sa_msgedit(request, msgid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = subemergency.objects.get(id=msgid)
    return render(request, 'subadmin/mssgedit.html', {"data": obj})


def sa_msgedit_post(request, msgid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    message = request.POST['textfield']
    subemergency.objects.filter(id=msgid).update(message=message)
    return HttpResponse('<script>alert("added");window.location="/subadmin_msgaddview#login"</script>')


def sa_msgdlt(request, msgid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    subemergency.objects.filter(id=msgid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/subadmin_msgaddview#login"</script>')


def subadmin_cmplrplyview(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = complaintesandreply.objects.filter(VOLUNTEER__SUBADMIN=request.session['subadminid'])
    return render(request, 'subadmin/com&rep.html', {"data": obj})


def subadmin_feedbackview(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = feedback.objects.filter(VOLUNTEER__SUBADMIN=request.session['subadminid'])
    return render(request, 'subadmin/feedback.html', {"data": obj})


def subadmin_chpass(request):
    return render(request, 'subadmin/changepass.html')


def chpass_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    LOGINID = request.session['lid']
    cp = request.POST['textfield']
    np = request.POST['textfield2']
    cop = request.POST['textfield3']
    q = login.objects.filter(password=cp, id=LOGINID)
    if q.exists():
        if np == cop:
            q.update(password=np)
            return HttpResponse(
                '<script>alert("password changed succesfully");window.location="/subadmin_chpass"</script>')
        else:
            return HttpResponse('<script>alert("Not match");window.location="/subadmin_chpass"</script>')
    else:
        return HttpResponse('<script>alert("Current password mismatch");window.location="/subadmin_chpass"</script>')


def sa_rply(request, cid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'subadmin/reply.html', {"data": cid})

def sub_userdb_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = userdb.objects.filter(VOLUNTEER=request.session['vid'])
    return render(request, 'subadmin/userdbview.html', {"data": obj})


def rply_post(request, cid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    message = request.POST['textfield']
    da = datetime.now().strftime("%d-%m-%Y")
    complaintesandreply.objects.filter(id=cid).update(reply=message, replydate=da)
    return HttpResponse('<script>alert("added");window.location="/subadmin_cmplrplyview#login"</script>')


def sa_alert_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = alert.objects.all()
    return render(request, 'subadmin/view.html', {"data": obj})


def subadmin_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    return render(request, 'subadmin/home.html')


def vol_admin_msg_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    v = volunteer.objects.get(id=request.session['vid'])
    obj = subemergency.objects.filter(SUBADMIN=v.SUBADMIN_id)
    return render(request, 'VOLUNTEER/msg.html', {"data": obj})


def slot_add(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'VOLUNTEER/slot.html')


def slotadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    totalslot = request.POST['textfield']
    currentslot = request.POST['textfield2']
    s = SLOT.objects.filter(VOLUNTEER=request.session['vid'])
    if s.exists():
        return HttpResponse('<script>alert("You have ' + str(
            s[0].currentslot) + ' available slot please checkout");window.location="/vol_slot_view#login"</script>')
    obj = SLOT()
    obj.totalslot = totalslot
    obj.currentslot = currentslot
    obj.VOLUNTEER_id = request.session['vid']
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/slot_add"</script>')


def vol_slot_edit(request, volid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = SLOT.objects.get(id=volid)
    return render(request, 'VOLUNTEER/edit.html', {"data": obj})


def vol_slotedit_post(request, volid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    totalslot = request.POST['textfield']
    currentslot = request.POST['textfield2']
    SLOT.objects.filter(id=volid).update(totalslot=totalslot, currentslot=currentslot)
    return HttpResponse('<script>alert("Updated");window.location="/vol_slot_view#login"</script>')


def vol_slot_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    try:
        obj = SLOT.objects.get(VOLUNTEER=request.session['vid'])
        return render(request, 'VOLUNTEER/SLOTVIEW.html', {"i": obj})
    except Exception as e:
        return render(request, 'VOLUNTEER/SLOTVIEW.html')


def VOL_SLOdlt(request, volid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    SLOT.objects.filter(id=volid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/vol_slot_view#login"</script>')


def need_add(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'VOLUNTEER/needadd.html')


def needadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    list = request.POST['textfield']
    quantityt = request.POST['textfield']
    obj = needs()
    obj.list = list
    obj.quantityt = quantityt
    obj.VOLUNTEER_id = request.session['vid']
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/vol_need_view#login"</script>')


def vol_need_edit(request, volid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = needs.objects.get(id=volid)
    return render(request, 'VOLUNTEER/neededit.html', {"data": obj})


def vol_need_post(request, volid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    list = request.POST['textfield']
    quantityt = request.POST['textfield2']
    needs.objects.filter(id=volid).update(list=list, quantityt=quantityt)

    return HttpResponse('<script>alert("added");window.location="/vol_need_view#login"</script>')


def vol_need_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = needs.objects.filter(VOLUNTEER=request.session['vid'])
    return render(request, 'VOLUNTEER/needview.html', {"data": obj})


def VOL_needdlt(request, volid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    needs.objects.filter(id=volid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/vol_need_view#login"</script>')


def filled(request, id):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    needs.objects.filter(id=id).update(status='filled')
    return HttpResponse('<script>alert("deleted");window.location="/vol_need_view#login"</script>')


def userdb_add(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    return render(request, 'VOLUNTEER/userdb.html')


def userdbadd_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    name = request.POST['textfield']
    age = request.POST['textfield2']
    phno = request.POST['textfield4']
    joiningdate = request.POST['textfield5']
    dismisaldate = request.POST['textfield6']
    if userdb.objects.filter(name=name, age=age, housename=request.POST['h'], post=request.POST['o'],
                             place=request.POST['p'], pin=request.POST['i'], phno=phno, joiningdate=joiningdate,
                             dismisaldate=dismisaldate, VOLUNTEER_id=request.session['vid']).exists():
        return HttpResponse('<script>alert("Already added");window.location="/vol_userdb_view#login"</script>')

    obj = userdb()
    obj.name = name
    obj.age = age
    obj.housename = request.POST['h']
    obj.post = request.POST['o']
    obj.place = request.POST['p']
    obj.pin = request.POST['i']
    obj.phno = phno
    obj.joiningdate = joiningdate
    obj.dismisaldate = dismisaldate
    obj.VOLUNTEER_id = request.session['vid']
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/vol_userdb_view#login"</script>')


def vol_userdb_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    obj = userdb.objects.filter(VOLUNTEER=request.session['vid'])
    return render(request, 'VOLUNTEER/userdbview.html', {"data": obj})


def VOL_userdb_dlt(request, volid):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    userdb.objects.filter(id=volid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/vol_userdb_view#login"</script>')


def feedback_snt(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'VOLUNTEER/feedback.html')


def feedbacksnt_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    feedback1 = request.POST['textarea']
    obj = feedback()
    obj.feedback = feedback1
    obj.VOLUNTEER = volunteer.objects.get(Login=request.session['lid'])
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/feedback_snt"</script>')


def cmplnt_snt(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    return render(request, 'VOLUNTEER/complaints.html')


def cmplntsnt_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')

    complaints1 = request.POST['textarea']
    obj = complaintesandreply()
    obj.complaints = complaints1
    obj.VOLUNTEER = volunteer.objects.get(Login=request.session['lid'])
    obj.save()
    return HttpResponse('<script>alert("added");window.location="/cmplnt_snt"</script>')


def vol_rply_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    data = complaintesandreply.objects.filter(VOLUNTEER=volunteer.objects.get(Login=request.session['lid']))
    return render(request, "VOLUNTEER/reply,html.html", {"data": data})


def vol_alert_view(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    obj = alert.objects.all()
    return render(request, 'VOLUNTEER/view.html', {"data": obj})


def vol_chpass(request):
    return render(request, 'VOLUNTEER/changepass.html')


def vol_chpass_post(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    LOGINID = request.session['lid']
    cp = request.POST['textfield']
    np = request.POST['textfield2']
    cop = request.POST['textfield3']
    q = login.objects.filter(password=cp, id=LOGINID)
    if q.exists():
        if np == cop:
            q.update(password=np)
            return HttpResponse('<script>alert("password changed succesfully");window.location="/vol_chpass"</script>')
        else:
            return HttpResponse('<script>alert("Not match");window.location="/vol_chpass"</script>')
    else:
        return HttpResponse('<script>alert("Current password mismatch");window.location="/vol_chpass"</script>')


def volunteer_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse('<script>alert("please login");window.location="/"</script>')
    return render(request, 'volunteer/home.html')


# =======================================================================================================================

def connect(request):
    return JsonResponse({"status": "ok"})


def nearestcamp(request):
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']

    ###### NEAR-BY code

    gcd_formula = "6371 * acos(least(greatest(cos(radians(%s)) * cos(radians('" + latitude + "')) * cos(radians('" + longitude + "') - radians(%s)) + sin(radians(%s)) * sin(radians('" + latitude + "')), -1), 1))"
    print(gcd_formula)
    qry = camp.objects.all()
    li = []
    for i in qry:
        qs = camp.objects.filter(id=i.id).annotate(
            distance=RawSQL(gcd_formula, (i.latitude, i.longitude, i.latitude))).order_by('distance')
        try:
            volunteerid = campallocation.objects.get(CAMP=camp.objects.get(id=i.id)).Volunteer_id
            res = SLOT.objects.get(VOLUNTEER=volunteerid)
            avs = int(res.totalslot) - int(res.currentslot)
        except:
            avs = "Not yet Updated"
        li.append({
            'name': i.name,
            'latitude': i.latitude,
            'longitude': i.longitude,
            "camp_distance": qs[0].distance,
            "slot": avs
        })

    #### Distance arranging.........................

    def camp_nearby_sort(e):
        return e['camp_distance']

    li.sort(key=camp_nearby_sort)
    # print("hhhhh",li[0:6])
    # for i in li[0:6]:
    print(li)
    return JsonResponse({"status": "ok", "users": li})



def viewneeds(request):
    users = []
    data = needs.objects.filter(~Q(status='filled'))
    for i in data:
        res = campallocation.objects.get(Volunteer=i.VOLUNTEER)
        campname = res.CAMP.name
        latitude = res.CAMP.latitude
        longitude = res.CAMP.longitude
        users.append({
            'list': i.list,
            'quantityt': i.quantityt,
            'date': i.date,
            'name': i.VOLUNTEER.name,
            'email': i.VOLUNTEER.email,
            'phone': i.VOLUNTEER.phone,
            'camp': campname,
            'latitude': latitude,
            'longitude': longitude,

        })
    print(users)
    return JsonResponse({"status": "ok", "users": users})


def viewprecautions(request):
    obj = precaution.objects.all().order_by('-id')
    arr = []
    for i in obj:
        arr.append({
            'description': i.description,
            'file': i.file,
        })
    print(arr)
    return JsonResponse({"status": "ok", "users": arr})


def viewalerts(request):
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    print("jfj", latitude, longitude)
    import requests
    URL = "https://api.weatherbit.io/v2.0/current?lat="+latitude+"&lon="+longitude+"&key=24891650caa74989b8d222818cb3836b"
    x = requests.get(URL)
    res = x.json()
    print(res)
    obj = alert.objects.all().order_by('-id')
    arr = []
    for i in obj:
        arr.append({"alert": i.alert})
    temp = res['data'][0]['app_temp']
    city = res['data'][0]['city_name']
    description = res['data'][0]['weather']['description']
    wind = res['data'][0]['wind_spd']
    return JsonResponse({"status": "ok", "data": arr, "temp": temp, "city": city, "description": description, "wind": wind})


def payment(request):
    name = request.POST['name']
    amount = request.POST['amount']
    obj = donation()
    obj.name = name
    obj.amount = amount
    obj.date = datetime.now().strftime("%Y-%m-%d")
    obj.save()
    return JsonResponse({"status": "ok"})