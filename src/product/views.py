from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.forms import addCropForm, addMachineForm
from product.models import Crop, Machinery

def index(request):
    if request.method == "GET":
        return render(request, 'index.html', context={})
    

def machinery(request):    
    if request.method == "GET":
        return render(request, 'machinery.html', context={})

def crops(request):
    if request.method == "GET":
        return render(request, 'crops.html', context={})
    
def offerCrop(request):    
    if request.method == "GET":
        return render(request, 'offeringC.html', context={})
    elif request.method == "POST":
        current_product=Crop()
        current_product.forename=request.POST['firstName']
        current_product.surname=request.POST['lastName']
        current_product.email=request.POST['userEmail']
        current_product.telephone  =request.POST['phoneNum']
        current_product.product=request.POST['prodName']
        current_product.price=request.POST['price']
        current_product.quantity=request.POST['quantity']
        current_product.production_date=request.POST['prodDate']
        current_product.condition    =request.POST['condition']
        current_product.location=request.POST['prodLocation']
        current_product.desc=request.POST['prodDescription']

        # current_product.title=myAddForm['title'].value()
        # current_product.desc=myAddForm['desc'].value()
        # current_product.price=myAddForm['price'].value()
        current_product.save()
        # return redirect(request, '/crops')
    
    return render(request, 'index.html', context={})
        
    
def offerMachine(request):    
    if request.method == "GET":
        return render(request, 'offeringM.html', context={})
    elif request.method == "POST":
        # myAddForm = addMachineForm(request.POST)
        # if myAddForm.is_valid():
        #     current_product = Machinery()
        #     current_product.forename=myAddForm['forename'].value()
        #     current_product.surname=myAddForm['surname'].value()
        #     current_product.email=myAddForm['email'].value()
        #     current_product.telephone  =myAddForm['telephone'].value()
        #     current_product.product=myAddForm['product'].value()
        #     current_product.price=myAddForm['price'].value()
        #     current_product.quantity=myAddForm['quantity'].value()
        #     current_product.production_date=myAddForm['production_date'].value()
        #     current_product.location=myAddForm['location'].value()
        #     current_product.condition    =myAddForm['condition'].value()
        #     current_product.desc=myAddForm['desc'].value()

        #     current_product.save()
        #     return redirect(request, '/crops/', context={"status":"PASS"})
        
      
        current_product = Machinery()
        current_product.forename=request.POST['firstName']
        current_product.surname=request.POST['lastName']
        current_product.email=request.POST['userEmail']
        current_product.telephone  =request.POST['phoneNum']
        current_product.product=request.POST['prodName']
        current_product.price=request.POST['price']
        current_product.quantity=request.POST['quantity']
        current_product.production_date=request.POST['prodDate']
        current_product.location=request.POST['prodLocation']
        current_product.condition    =request.POST['condition']
        current_product.desc=request.POST['prodDescription']

        current_product.save()

    return render(request, 'index.html', context={})

    
def seekCrops(request):    
    if request.method == "GET":
        crops = Crop.objects.all()
        return render(request, 'seekingC.html', context={"crops":crops})
    
def seekMachines(request):    
    if request.method == "GET":
        machineries = Machinery.objects.all()
        return render(request, 'seekingM.html', context={"machineries":machineries})
    
# def cropAdd(request):
#     return render(request, 'formpage.html', context={})



def addproduct(request):
    # title=""
    # desc=""
    # price=0.00
    if request.method=="POST":
        myAddForm=addCropForm(request.post)
        if myAddForm.is_valid():
            current_product=Crop()
            current_product.title=myAddForm['title'].value()
            current_product.desc=myAddForm['desc'].value()
            current_product.price=myAddForm['price'].value()
        current_product.save()
        return render(request, 'index.html', context={"status":"PASS"})
        # print(', '.join("%s: %s" % item for item in vars(myAddForm).items()))
        # print(Crop.objects.all())
    # elif request.method == "GET":
    # #    myAddForm=addCropForm()
    #     current_product=Crop.objects.first()
    #     print(', '.join("%s: %s" % item for item in vars(current_product).items()))

    return render(request, 'index.html', context={"FAIL":"BAD DATA", "MSG":"BAD DATA"})
