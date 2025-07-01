from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from YTweet import views as yt_views  # Rename for clarity

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page (shows tweet list or login/register forms)
    path('', yt_views.index, name='home'),

    # YTweet app routes
    path('YTweet/', include(('YTweet.urls', 'YTweet'), namespace='YTweet')),

    # Auth routes
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', yt_views.register, name='register'),]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
