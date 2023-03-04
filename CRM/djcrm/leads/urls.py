from django.urls import path 
from leads.views import (
    leads_page, lead_details, lead_create, lead_update, lead_delete, LeadListView, LeadDetailView, LeadCreateView,
    LeadUpdateView, LeadDeleteView
)
app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('create_leads/',LeadCreateView.as_view(), name='lead-create'),
]