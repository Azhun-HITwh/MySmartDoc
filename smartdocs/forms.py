from django.forms import ModelForm,  TextInput, FileInput, Select
from .models import Product, Category, Document, Related_object, Manufacturer, Doc_issued_by


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('author', 'create_date', 'mod_date')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'code': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '产品名称',
            'code': '产品代码',
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ('author', 'create_date', 'mod_date')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '类别',
        }


class ObjectForm(ModelForm):
    class Meta:
        model = Related_object
        exclude = ('author', 'create_date', 'mod_date')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '零件名',
        }


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        exclude = ('author', 'create_date', 'mod_date')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '制造商',
        }


class Doc_issued_byForm(ModelForm):
    class Meta:
        model = Doc_issued_by
        exclude = ('author', 'create_date', 'mod_date')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '文档发布者',
        }


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ('author', 'create_date', 'mod_date', 'product')

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'version_no': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'related_object': Select(attrs={'class': 'form-control'}),
            'vehicle_type': TextInput(attrs={'class': 'form-control'}),
            'doc_file': FileInput(attrs={'class': 'form-control'}),
            'issue_date': TextInput(attrs={'class': 'form-control'}),
            # 'status': Select(attrs={'class':'form-control'}),
            'manufacturer': Select(attrs={'class': 'form-control'}),
            'doc_issued_by': Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': '文档标题',
            'version_no': '版本号',
            'category': '文档类别',
            'related_object': '相关零件',
            'vehicle_type': '项目',
            'doc_file': '上传文件',
            'issue_date': '发布日期',
            'status': '有效',
            'manufacturer': '制造商',
            'doc_issued_by': '发布者',
        }

