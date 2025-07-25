from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static  # cấu hình phục vụ file media trong chế độ phát triển
from django.conf import settings   # Truy cập các thiết lập từ settings.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Thêm đường dẫn để Django có thể phục vụ các tệp media (ảnh, video, v.v.) trong chế độ phát triển (DEBUG=True)
