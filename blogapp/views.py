from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from blogapp.models import mobile
from blogapp.forms import blogappForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from userprofile.models import profile
# Create your views here.

def blogapp(request):
    return render(request, "index.html")


def about(request):
    data = mobile.objects.all()
    print(data)
    context = {"data": data}
    return render(request, "about.html", context)

def form(request):
    data = mobile.objects.all()
    print(data)
    context = {"data": data}
    return render(request, "form.html", context)

def blogapp(request):
    data = mobile.objects.all()
    print(data)
    context = {"data": data}
    return render(request, "index.html", context)


def home(request):
    data = mobile.objects.all()
    print(data)
    context = {"data": data}
    return render(request, "index.html", context)

def details(request):
    data = mobile.objects.all()
    print(data)
    context = {"data": data}
    return render(request, "details.html", context)



def add_product(request):
    return render(request, "form.html")



def add_product(request):
    form = blogappForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        mobile.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(reverse("blogapp:blogapp"))
    return render(request, "form.html", {"form": form})



class Addproductview(LoginRequiredMixin, CreateView):
    model = mobile
    form_class = blogappForm
    template_name = 'form.html'




def edit_product(request, product_id):
    photo = mobile.objects.get(id=product_id)
    form = blogappForm(request.POST or None, request.FILES or None, instance=photo)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("blogapp:blogapp"))
    return render(request, "form.html", {"form":form})


def delete_product(request, product_id):
    pproduct = get_object_or_404(mobile, id=product_id)
    pproduct.delete()
    return HttpResponseRedirect(reverse("blogapp:blogapp"))



def created_by_user(request):
    data = mobile.objects.filter(person="admin")
    print(data)
    context = {"data": data}
    return render(request, "created_by.html", context)

def usercreated(request):
    data = mobile.objects.filter(person="suyog")
    print(data)
    context = {"data": data}
    return render(request, "usercreated.html", context)




def storage(request):
    data = mobile.objects.filter(storage="32GB")
    print(data)
    context = {"data": data}
    return render(request, "storage.html", context)



def storage1(request):
    data = mobile.objects.filter(storage="64GB")
    print(data)
    context = {"data": data}
    return render(request, "storage1.html", context)