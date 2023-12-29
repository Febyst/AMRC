import smtplib


from django.shortcuts import render

from AMapp.models import Contact, customers
from AMproject import settings


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
def hatchback(request):
    return render(request, "hatchback.html")
def sedan(request):
    return render(request, "sedan.html")
def suv(request):
    return render(request, "suv.html")
def booking(request):
    return render(request, "booking.html")
def register(request):

    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        addr = request.POST['address']
        city = request.POST['city']
        mail = request.POST['eaddress']
        zip = request.POST['zip']
        state = request.POST['state']
        phone = request.POST['phone']
        checkindate = request.POST['checkindate']
        checkoutdate = request.POST['checkoutdate']
        driver = request.POST['cdrivers']
        airport = request.POST['apt']
        vehicletype = request.POST['vtype']
        vehiclemode = request.POST['vmode']
        transmission = request.POST['trans']
        specialinstructions = request.POST['splints']

        customers(c_fname = firstname,c_lname = lastname,c_addr = addr,c_city = city,c_mail = mail,c_zip = zip,c_state = state,c_phone = phone,c_cindate = checkindate,c_coutdate = checkoutdate,c_driver = driver,c_apt = airport,c_vtype = vehicletype,c_vmod = vehiclemode,c_trans = transmission,c_splints = specialinstructions).save()

    return render(request,"register.html")

def contact(request):
    if request.method == "POST":
        contact : Contact = Contact()
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        type = request.POST.get('ctype')
        message = request.POST.get('cmessage')

        contact.c_name = name
        contact.c_email = email
        contact.c_type = type
        contact.c_message = message
        contact.save()
        email_from = settings.EMAIL_HOST_USER
        passw = settings.EMAIL_HOST_PASSWORD
        recipient_list = contact.c_email
        message = contact.c_message
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_from, passw)
            server.sendmail(recipient_list,email_from, message)
            server.quit()
        return render(request, 'success.html')
    return render(request, "contact.html")

def success(request):
    return render(request,"success.html")