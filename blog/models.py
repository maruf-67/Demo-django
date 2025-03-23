from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)  # Increased from default 50 to 255author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = QuillField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from title and truncate to max_length
            base_slug = slugify(self.title)
            slug = base_slug[:255]
            # Ensure uniqueness
            counter = 1
            original_slug = slug
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{original_slug[:250]}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"