from django.shortcuts import render
from .models import Form, Residence, Ownership, ServiceDetail
# Create your views here.


def index(request):
    form = Form.objects.all()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def form(request):
    return render(request, 'form.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']


        info = Form(name=name, email=email, password=password)
        info.save()

        return render(request, 'submit.html')

def formSubmit(request):
    name = request.POST['name']
    ward = request.POST['ward']
    tname = request.POST['tname']
    hnumber = request.POST['hnumber']
    gender = request.POST['gender']
    religeous = request.POST['religeous']
    language = request.POST['language']
    ownertype = request.POST['ownertype']
    housetype = request.POST['housetype']
    landtype = request.POST['landtype']
    totalroom = request.POST['totalroom']
    houseused = request.POST['houseused']
    housearea = request.POST['housearea']
    earthquake = request.POST['earthquake']
    radio = request.POST['radio']
    tv = request.POST['tv']
    computer = request.POST['computer']
    mobile = request.POST['mobile']
    internet = request.POST['internet']
    motercycle = request.POST['motercycle']
    car = request.POST['car']
    hitar = request.POST['hitar']

    def count(n):
        for i in range(n):
            return i
            if i == n:
                return n+1

    ownership = Ownership.objects.create(house_no=hnumber, ward_no=ward, tole=tname, house_owner=name, gender=gender, religion=religeous, language=language)
    ownership.save()

    residence = Residence.objects.create(ownership_type=ownertype, house_type=housetype, land_type=landtype, total_room=totalroom, house_use=houseused, house_area=housearea, earthquake_resistance=earthquake)
    residence.save()

    serviceDetail = ServiceDetail.objects.create(radio=radio, television=tv, computer=computer, internet= internet, motorcycle=motercycle, car=car, heater=hitar)
    serviceDetail.save()

    return render(request, 'submit.html')
