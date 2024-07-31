from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Person
from .forms import PersonForm

class HomeView(TemplateView):
    template_name = 'tenant_blog/home.html'

class PersonListView(ListView):
    model = Person
    template_name = 'tenant_blog/person_list.html'
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'tenant_blog/person_form.html'
    success_url = reverse_lazy('person-list')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'tenant_blog/person_form.html'
    success_url = reverse_lazy('person-list')

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'tenant_blog/person_confirm_delete.html'
    success_url = reverse_lazy('person-list')
