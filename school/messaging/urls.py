from django.urls import path
from . import views

urlpatterns = [
    # Messagerie
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('compose/', views.compose, name='compose'),
    path('message/<int:pk>/', views.message_detail, name='message_detail'),
    path('message/<int:pk>/delete/', views.delete_message, name='delete_message'),
    
    # Annonces
    path('announcements/', views.announcements, name='announcements'),
    path('announcements/create/', views.create_announcement, name='create_announcement'),
    path('announcements/<int:pk>/delete/', views.delete_announcement, name='delete_announcement'),
]
