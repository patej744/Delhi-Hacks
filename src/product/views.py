from django.shortcuts import render
from django.http import HttpResponse
from product.forms import addCropForm 
from product.models import Crop

def index(request):
    return render(request, 'index.html', context={})
def cropAdd(request):
    return render(request, 'formpage.html', context={})
def addproduct(request):
    print("here")
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
