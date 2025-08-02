from .views import ProfileView
from .views import ProfileEditView
from django.urls import path

urlpatterns = [

    path('profile/<slug:username>/', ProfileView.as_view(), name='profile'),

    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),

]
