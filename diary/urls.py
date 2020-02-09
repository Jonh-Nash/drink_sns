from django.urls import path

from . import views


app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>', views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>', views.DiaryDeleteView.as_view(), name="diary_delete"),
    path('diary-alllist/', views.DiaryAlllistView.as_view(), name="diary_alllist"),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('want/<int:pk>', views.wantfunc, name='want'),
    path('diary-map/', views.DiaryMap.as_view(), name="diary_map"),
    path('easy-login', views.easyfunc, name='easy_login'),
]
