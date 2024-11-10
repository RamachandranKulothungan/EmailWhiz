
from django.contrib import admin
from django.urls import path, include

from emailwhiz_api import views as views
from emailwhiz_ui import views as ui_views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path, include
from emailwhiz_ui.views import register_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ui_views.home, name='home'),
    path('list-resumes/', ui_views.list_resumes, name='list_resumes'),
    path('select-template/', ui_views.select_template, name='select_template'),
    path('upload-excel/', ui_views.upload_excel, name='upload_excel'),
    path('preview-template/', ui_views.preview_template, name='preview_template'),
    # path('', include('emailwhiz_ui.urls')),
    path('generate_template/', views.generate_template, name='generate_template'),
    path('send_email/', views.send_email, name='send_email')
    path('ui/', include('emailwhiz_ui.urls')),
    path('', lambda request: redirect('login')),
    path('register/', register_view, name='register')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

