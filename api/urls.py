from django.urls import path, include
from .views import fighter_list, fighter_detail, FighterAPIView,FighterDetailAPIView, GenericAPIView

urlpatterns = [
    #path('fighter/', fighter_list),
    path('fighter/', FighterAPIView.as_view()),
    #path('fighter/<int:pk>/', fighter_detail)
    path('fighter/<int:id>/', FighterDetailAPIView.as_view()),
    path('generic/fighter/<int:id>/', GenericAPIView.as_view()),
]
