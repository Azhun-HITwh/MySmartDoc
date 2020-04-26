from django.shortcuts import render

# Create your views here.

from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from .models import Product, Category, Document, Related_object, Manufacturer, Doc_issued_by
from .forms import ProductForm, CategoryForm, DocumentForm, ObjectForm, ManufacturerForm, Doc_issued_byForm
from django.db.models import Q

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


@method_decorator(login_required, name='dispatch')
# @method_decorator(permission_required('smartdocs.add_product', raise_exception=True), name='dispatch')
class ProductCreate(CreateView):
    model = Product
    template_name = 'smartdocs/form.html'
    form_class = ProductForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
# @method_decorator(permission_required('smartdocs.change_product', raise_exception=True), name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    template_name = 'smartdocs/form.html'
    form_class = ProductForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.author != self.request.user:
            raise Http404()
        return obj


class CategoryList(ListView):
    model = Category


class CategoryDetail(DetailView):
    model = Category


@method_decorator(login_required, name='dispatch')
class CategoryCreate(CreateView):
    model = Category
    template_name = 'smartdocs/form.html'
    form_class = CategoryForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CategoryUpdate(UpdateView):
    model = Product
    template_name = 'smartdocs/form.html'
    form_class = CategoryForm


class ObjectList(ListView):
    model = Related_object


class ObjectDetail(DetailView):
    model = Related_object


@method_decorator(login_required, name='dispatch')
class ObjectCreate(CreateView):
    model = Related_object
    template_name = 'smartdocs/form.html'
    form_class = ObjectForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ObjectUpdate(UpdateView):
    model = Related_object
    template_name = 'smartdocs/form.html'
    form_class = ObjectForm


class ManufacturerList(ListView):
    model = Manufacturer


class ManufacturerDetail(DetailView):
    model = Manufacturer


@method_decorator(login_required, name='dispatch')
class ManufacturerCreate(CreateView):
    model = Manufacturer
    template_name = 'smartdocs/form.html'
    form_class = ManufacturerForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    template_name = 'smartdocs/form.html'
    form_class = ManufacturerForm


class Doc_issued_byList(ListView):
    model = Doc_issued_by


class Doc_issued_byDetail(DetailView):
    model = Doc_issued_by


@method_decorator(login_required, name='dispatch')
class Doc_issued_byCreate(CreateView):
    model = Doc_issued_by
    template_name = 'smartdocs/form.html'
    form_class = Doc_issued_byForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class Doc_issued_byUpdate(UpdateView):
    model = Doc_issued_by
    template_name = 'smartdocs/form.html'
    form_class = Doc_issued_byForm


class DocumentList(ListView):
    model = Document


class DocumentDetail(DetailView):
    model = Document


@method_decorator(login_required, name='dispatch')
class DocumentCreate(CreateView):
    model = Document
    template_name = 'smartdocs/form.html'
    form_class = DocumentForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product = Product.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DocumentUpdate(UpdateView):
    model = Document
    template_name = 'smartdocs/form.html'
    form_class = DocumentForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.author != self.request.user:
            raise Http404()
        return obj


@csrf_exempt
def document_search(request):
    q = request.GET.get('q', None)
    if q:
        document_list = Document.objects.filter(Q(title__icontains=q) |
                                                Q(product__name__icontains=q) |
                                                Q(product__code__icontains=q))
        context = {'document_list': document_list}
        return render(request, 'smartdocs/document_search.html', context)

    return render(request, 'smartdocs/document_search.html',)


@csrf_exempt
def doc_ajax_search(request):
    q = request.GET.get('q', None)
    if q:
        document_list = Document.objects.filter(Q(title__icontains=q) |
                                                Q(product__name__icontains=q) |
                                                Q(product__code__icontains=q))
        data = []
        for document in document_list:
            data.append({"title": document.title, "product_name": document.product.name,
                        "category_name": document.category.name,
                         "format": document.doc_file.url.split('.')[-1].upper(),
                         "size": "{:.1f}KB".format(document.doc_file.size/1024),
                         "version": document.version_no, "date": document.mod_date,
                         "product_id": document.product.id, "id": document.id,
                         "url": document.doc_file.url,
                         })
        json_data = json.dumps(data, cls=MyEncoder)

        return HttpResponse(json_data)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')

        return json.JSONEncoder.default(self, obj)

