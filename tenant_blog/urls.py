# tenant_blog/urls.py
from django.urls import path
from .views import PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView,HomeView

urlpatterns = [
    path('people/', PersonListView.as_view(), name='person-list'),
    path('people/create/', PersonCreateView.as_view(), name='person-create'),
    path('people/<int:pk>/update/', PersonUpdateView.as_view(), name='person-update'),
    path('people/<int:pk>/delete/', PersonDeleteView.as_view(), name='person-delete'),
    path('' , HomeView.as_view(), name='home'),
]
