from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static  # cấu hình phục vụ file media trong chế độ phát triển
from django.conf import settings   # Truy cập các thiết lập từ settings.py
from blogs import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('category/', include('blogs.urls')),
    path('<slug:slug>/', BlogsView.blogs, name='blogs' )
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Thêm đường dẫn để Django có thể phục vụ các tệp media (ảnh, video, v.v.) trong chế độ phát triển (DEBUG=True)
