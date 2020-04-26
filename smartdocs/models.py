from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os
import uuid


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif"]:
        sub_folder = "picture"
    if ext.lower() in ["pdf", "docx", "txt"]:
        sub_folder = "document"
    return os.path.join(str(instance.author.id), sub_folder, filename)


class AbstractModel(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Product(AbstractModel):
    """产品"""
    name = models.TextField(max_length=30, verbose_name='Product Name',)
    code = models.TextField(max_length=30, blank=True, default='', verbose_name='Product Code',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('smartdocs:product_detail', args=[str(self.id)])

    @property
    def document_count(self):
        return Document.objects.filter(product_id=self.id).count()

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "产品"
        verbose_name_plural = '产品'


class Category(AbstractModel):
    """文档类型"""
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('smartdocs:category_detail', args=[self.id])

    @property
    def document_count(self):
        return Document.objects.filter(category_id=self.id).count()

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "文档分类"
        verbose_name_plural = '文档分类'


class Vehicle_type(AbstractModel):
    """项目"""
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "项目"
        verbose_name_plural = "项目"


class Related_object(AbstractModel):
    """相关零件"""
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('smartdocs:object_detail', args=[self.id])

    @property
    def document_count(self):
        return Document.objects.filter(related_object_id=self.id).count()

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "相关零件"
        verbose_name_plural = "相关零件"


class Manufacturer(AbstractModel):
    """制造商"""
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('smartdocs:manufacturer_list', args=[self.id])

    @property
    def document_count(self):
        return Document.objects.filter(manufacturer_id=self.id).count()

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "制造商"
        verbose_name_plural = "制造商"


class Doc_issued_by(AbstractModel):
    """文档发布者"""
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('smartdocs:doc_issued_by_list', args=[self.id])

    @property
    def document_count(self):
        return Document.objects.filter(doc_issued_by_id=self.id).count()

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "文档发布者"
        verbose_name_plural = "文档发布者"


class Document(AbstractModel):
    """文档"""
    title = models.TextField(max_length=30, verbose_name='Title',)
    version_no = models.IntegerField(blank=True, default=1, verbose_name='Version No.',)
    doc_file = models.FileField(upload_to=user_directory_path, blank=True, null=True,)
    issue_date = models.DateField(verbose_name='Issue Date',)
    status = models.BooleanField(default=True,)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='documents',)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='documents',)
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE, related_name='documents',)
    related_object = models.ForeignKey(Related_object, on_delete=models.CASCADE, related_name='documents',)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='documents',)
    doc_issued_by = models.ForeignKey(Doc_issued_by, on_delete=models.CASCADE, related_name='documents',)

    def __str__(self):
        return self.title

    def get_format(self):
        return self.doc_file.url.split('.')[-1].upper()

    def get_absolute_url(self):
        return reverse('smartdocs:document_detail', args=[str(self.product.id), str(self.id)])

    class Meta:
        ordering = ['-mod_date']
        verbose_name = "文档"
        verbose_name_plural = '文档'
