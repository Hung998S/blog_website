from django.db import models
from django.contrib.auth.models import User

# Tạo các model (bảng trong cơ sở dữ liệu) tại đây.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True) # Tên danh mục, tối đa 50 ký tự, không được trùng lặp
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo, tự động gán khi bản ghi được tạo lần đầu
    updated_at = models.DateTimeField(auto_now=True)      # Thời gian cập nhật, tự động cập nhật mỗi khi bản ghi được lưu
    
    def __str__(self):
        return self.category_name  # Giúp hiển thị rõ tên danh mục trong admin
    
    class Meta:
        # verbose_name_plural dùng để định nghĩa tên số nhiều cho model trong Django Admin
        # Mặc định Django sẽ thêm 's' vào tên model, nhưng với từ không theo quy tắc số nhiều
        # ta dùng verbose_name_plural để sửa lại cho đúng (ví dụ: 'Categories' thay vì 'Categorys')
        verbose_name_plural = 'Categories'
        
STATUS_CHOICE = (
    ('draft','Draft'),       # 'draft' dùng để lưu trạng thái nháp, hiển thị là 'Draft'
    ('published','Published')   # 'public' dùng cho bài viết đã xuất bản, hiển thị là 'Published'
)

class Blogs(models.Model):
    title = models.CharField(max_length=100, unique=True)  # Tiêu đề bài viết, tối đa 100 ký tự, không trùng
    slug = models.SlugField(unique=True, blank=True)       # Đường dẫn thân thiện, không trùng, cho phép bỏ trống
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Liên kết đến danh mục, xóa danh mục thì bài viết cũng bị xóa
    author = models.ForeignKey(User, on_delete=models.CASCADE)        # Liên kết đến người dùng (tác giả)
    blog_image = models.ImageField(upload_to='uploads/%y/%m/%d')      # Hình ảnh bài viết, lưu theo thư mục năm/tháng/ngày
    short_description = models.TextField(max_length=1000)             # Mô tả ngắn gọn bài viết, tối đa 1000 ký tự
    blog_body = models.TextField(max_length=3000)                     # Nội dung đầy đủ của bài viết, tối đa 3000 ký tự
    status = models.CharField(max_length = 100,choices = STATUS_CHOICE, default = 'draft')  # Trạng thái bài viết: nháp hoặc đã đăng
    is_feacherd = models.BooleanField(default=False)                  # Đánh dấu bài viết có phải là nổi bật không (nên sửa thành is_featured)
    created_at = models.DateTimeField(auto_now_add=True)              # Ngày tạo bài viết, tự động thêm khi tạo
    updated_at = models.DateTimeField(auto_now=True)                  # Ngày cập nhật bài viết, tự động thay đổi khi lưu

    class Meta:
        verbose_name_plural = 'Blogs'
        
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete = models.CASCADE)
    comment = models.TextField(max_length=250)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.comment