from django.urls import path 
from leads.views import leads_page, lead_details, lead_create, lead_update, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', leads_page, name='lead-list'),
    path('<int:pk>/', lead_details, name='lead-detail'),
    path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('create_leads/',lead_create, name='lead-create'),
]