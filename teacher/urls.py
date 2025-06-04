from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('add_or_update_student/', views.add_or_update_student, name='add_or_update_student'),
    path('update_student/<int:pk>/', views.update_student_ajax, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('register/', views.register_staff, name='register_staff'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]