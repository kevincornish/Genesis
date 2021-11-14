from django.db import models

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class Torrent(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, blank=True)
    uploaded_by = models.CharField(max_length=25)
    torrent_path = models.FileField(upload_to='torrents/')
    uploaded_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name