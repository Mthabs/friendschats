from django.urls import path
from .views import LikeListCreateView, LikeDetailView  

urlpatterns = [
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),
]