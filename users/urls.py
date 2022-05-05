from django.urls import path
from .views import MoviesView, CollectionsView,RegisterApi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='user_register'),
    path('movies/', MoviesView.as_view(), name='movies_list'),
    path('collection/', CollectionsView.as_view(), name='collections_list'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #path('api/register', RegisterApi.as_view()),
]
