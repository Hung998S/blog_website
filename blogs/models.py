from django.db import models

# Tạo các model (bảng trong cơ sở dữ liệu) tại đây.
class Category(models.Model):
    # Tên danh mục, tối đa 50 ký tự, không được trùng lặp
    category_name = models.CharField(max_length=50, unique=True)
    
    # Thời gian tạo, tự động gán khi bản ghi được tạo lần đầu
    create_at = models.DateTimeField(auto_now_add=True)

    # Thời gian cập nhật, tự động cập nhật mỗi khi bản ghi được lưu
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        # verbose_name_plural dùng để định nghĩa tên số nhiều cho model trong Django Admin
        # Mặc định Django sẽ thêm 's' vào tên model, nhưng với từ không theo quy tắc số nhiều
        # ta dùng verbose_name_plural để sửa lại cho đúng (ví dụ: 'Categories' thay vì 'Categorys')
        verbose_name_plural = 'Categories'