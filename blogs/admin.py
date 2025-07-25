from django.contrib import admin
from . models import Category ,Blogs # Import model Category từ app hiện tại

# Đăng ký model Category để hiển thị trong trang quản trị Django admin

class CategoryAdmin(admin.ModelAdmin):
    # list_display: hiển thị các trường này trong danh sách các đối tượng Category trên trang admin
    list_display = ('id', 'category_name', 'created_at', 'updated_at')
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    prepopulated_fields = {'slug':('title')}   # prepopulated_fields: Tự động điền trường 'slug' dựa theo nội dung của 'title'

# Đăng ký model Category với giao diện quản trị, sử dụng class CategoryAdmin để tùy chỉnh
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs)