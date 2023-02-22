

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from apps.common.views import home ,SingUpView ,dashbordView ,ProfileUpdateView,ProfileView,clientView,societeView,ajoutView,ContacterView,pisteView,messageView,delete_client,piplineView,repondreView,UpdateClientView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.as_view(),name='home'),
    path('register/',SingUpView.as_view(),name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='common/login.html'),
    name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'),
    name='logout'),
    path('dashbord/',dashbordView.as_view(),name='dashbord'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='common/change-password.html',
        success_url='/'),
    name='change-password'),
     # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('client/', clientView.as_view(), name='client'),
    path('societe/', societeView.as_view(), name='societe'),
    path('ajout/', ajoutView.as_view(), name='ajout'),
    path('contacter/', ContacterView.as_view(), name='contacter'),
    path('piste/', pisteView.as_view(), name='piste'),
    path('message/<str:firstname>/', messageView.as_view(), name='message'), 
    path('client/<int:id>/delete/', delete_client, name='delete_client'),
    path('pipline/', piplineView.as_view(), name='pipline'),
    path('repondre/', repondreView.as_view(), name='repondre'),
    path('client/<int:id>/update/', UpdateClientView.as_view(), name='update_client'),
]

from django.conf import settings 
from django.conf.urls.static import static 

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)