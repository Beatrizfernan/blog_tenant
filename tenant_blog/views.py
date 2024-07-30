from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'tenant_blog/person_list.html'

    def get_queryset(self):
        return Person.objects.filter(tenant=self.request.tenant)


class PersonCreateView(CreateView):
    model = Person
    template_name = 'tenant_blog/person_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth']

    def form_valid(self, form):
        form.instance.tenant = self.request.tenant
        return super().form_valid(form)

class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'tenant_blog/person_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth']

    def get_queryset(self):
        return Person.objects.filter(tenant=self.request.tenant)

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'tenant_blog/person_confirm_delete.html'
    success_url = reverse_lazy('person-list')

    def get_queryset(self):
        return Person.objects.filter(tenant=self.request.tenant)
