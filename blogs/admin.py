from django.contrib import admin
from . models import Category  # Import model Category từ app hiện tại

# Đăng ký model Category để hiển thị trong trang quản trị Django admin

class CategoryAdmin(admin.ModelAdmin):
    # list_display: hiển thị các trường này trong danh sách các đối tượng Category trên trang admin
    list_display = ('id', 'category_name', 'created_at', 'updated_at')

# Đăng ký model Category với giao diện quản trị, sử dụng class CategoryAdmin để tùy chỉnh
admin.site.register(Category, CategoryAdmin)
