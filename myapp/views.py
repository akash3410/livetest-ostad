from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import AddContact, UpdateForm

# Create your views here.
def home_page(request):
    contacts = Contact.objects.all()
    return render(request, "index.html", {"contacts": contacts})

def add_contact(request):
    if request.method == 'POST':
        form = AddContact(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('home_page')
    else:
        form = AddContact()

    return render(request, 'add_contact.html', {'form': form})

def contact_details(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, "contact_details.html", {"contact": contact})

def delete_con(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect("home_page")

def update_contact(request, pk):
    employee = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = UpdateForm(instance=employee)

    return render(request, 'update_contact.html', {'form': form})
