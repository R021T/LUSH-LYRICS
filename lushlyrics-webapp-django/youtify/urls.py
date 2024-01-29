from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from accounts.views import loginUser, createUser, logoutUser
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # User authentication routes
    path('accounts/login/', loginUser, name='login'),
    path('accounts/logout', logoutUser, name='logout'),
    path('accounts/create', createUser, name='signup'),
    # path('accounts/users/<pk>', userDetails, name='userDetails'),
    # path('accounts/delete/<pk>', deleteUser, name='deleteUser'),
    
    # Password reset routes
    path('accounts/reset-password', PasswordResetView.as_view(), name="password_reset"),
    path('accounts/reset-password/done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('accounts/reset-password/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('accounts/reset-password/complete', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path("", views.default, name='home'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page')
]
