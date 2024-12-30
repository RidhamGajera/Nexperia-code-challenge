from django.urls import path
from .views import EmailCampaignView

urlpatterns = [
    path('', EmailCampaignView.as_view(), name='create_campaign'),
]
