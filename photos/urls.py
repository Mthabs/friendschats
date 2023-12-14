from django.urls import path
from .views import PhotoListCreateView, PhotoDetailView, PhotoLikeView, PhotoUnlikeView

urlpatterns = [
    path('photos/', PhotoListCreateView.as_view(), name='photo-list-create'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('photos/<int:pk>/like/', PhotoLikeView.as_view(), name='photo-like'),
    path('photos/<int:pk>/unlike/', PhotoUnlikeView.as_view(), name='photo-unlike'),
]