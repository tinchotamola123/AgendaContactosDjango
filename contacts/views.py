from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Contact
from django.urls import reverse_lazy

# Create your views here.

class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 4
    
    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')
        if q:
            return Contact.objects.filter(name__icontains=q)
        
        return super().get_queryset()
    
    
class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('avatar','name', 'email', 'birth', 'phone',)
    success_url = reverse_lazy('contact_list')


class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('avatar','name', 'email', 'birth', 'phone',)
    success_url = reverse_lazy('contact_list')
    
class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')