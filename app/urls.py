from django.urls import path,include
from app import views 
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('', views.ProductView.as_view(), name='home'),
   
    path('address', views.address, name='address'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('login', views.login, name='login'),
    path('registration', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view
    (template_name='app/login.html',
    authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    

    path('passwordchange/', auth_views.PasswordChangeView.as_view(
        template_name = 'app/passwordchange.html',
        form_class= MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name = 'app/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name = 'app/password_reset.html', 
        form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'app/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'app/password_reset_confirm.html',
        form_class=MySetPasswordForm
        ),name='password_reset_confirm'),

    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'app/password_reset_complete.html'),name='password_reset_complete'),
    
    # path('profile', auth_views.Profile.as_view(),name='profile'),
    path('profile/', views.HomeView.as_view(), name='profile'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate'),

    
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

