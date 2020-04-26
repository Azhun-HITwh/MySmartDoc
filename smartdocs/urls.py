from django.urls import path, re_path
from . import views

# namespace
app_name = 'smartdocs'

urlpatterns = [

    # 展示产品列表
    path('product/', views.ProductList.as_view(), name='product_list'),

    # 展示产品详情
    re_path(r'^product/(?P<pk>\d+)/$',
            views.ProductDetail.as_view(), name='product_detail'),

    # 创建产品
    re_path(r'^product/create/$',
            views.ProductCreate.as_view(), name='product_create'),

    # 修改产品
    re_path(r'^product/(?P<pk>\d+)/update/$',
            views.ProductUpdate.as_view(), name='product_update'),

    # 展示类别列表
    path('category/', views.CategoryList.as_view(), name='category_list'),

    # 展示类别详情
    re_path(r'^category/(?P<pk>\d+)/$',
            views.CategoryDetail.as_view(), name='category_detail'),

    # 创建类别
    re_path(r'^category/create/$',
            views.CategoryCreate.as_view(), name='category_create'),

    # 修改类别
    re_path(r'^category/(?P<pk>\d+)/update/$',
            views.CategoryUpdate.as_view(), name='category_update'),

    # 创建相关零件
    re_path(r'^object/create/$',
            views.ObjectCreate.as_view(), name='object_create'),

    # 修改相关零件
    re_path(r'^object/(?P<pk>\d+)/update/$',
            views.ObjectUpdate.as_view(), name='object_update'),

    # 展示相关零件详情
    re_path(r'^object/(?P<pk>\d+)/$',
            views.ObjectDetail.as_view(), name='object_detail'),

    # 展示相关零件列表
    path('object/', views.ObjectList.as_view(), name='object_list'),

    # 创建制造商
    re_path(r'^manufacturer/create/$',
            views.ManufacturerCreate.as_view(), name='manufacturer_create'),

    # 修改制造商
    re_path(r'^manufacturer/(?P<pk>\d+)/update/$',
            views.ManufacturerUpdate.as_view(), name='manufacturer_update'),

    # 展示制造商详情
    re_path(r'^manufacturer/(?P<pk>\d+)/$',
            views.ManufacturerDetail.as_view(), name='manufacturer_detail'),

    # 展示制造商列表
    path('manufacturer/', views.ManufacturerList.as_view(), name='manufacturer_list'),

    # 创建文档发布者
    re_path(r'^doc_issued_by/create/$',
            views.Doc_issued_byCreate.as_view(), name='doc_issued_by_create'),

    # 修改文档发布者
    re_path(r'^doc_issued_by/(?P<pk>\d+)/update/$',
            views.Doc_issued_byUpdate.as_view(), name='doc_issued_by_update'),

    # 展示文档发布者详情
    re_path(r'^doc_issued_by/(?P<pk>\d+)/$',
            views.Doc_issued_byDetail.as_view(), name='doc_issued_by_detail'),

    # 展示文档发布者列表
    path('doc_issued_by/', views.Doc_issued_byList.as_view(), name='doc_issued_by_list'),

    # 展示文档列表
    path('document/', views.DocumentList.as_view(), name='document_list'),

    # 展示文档详情
    re_path(r'^product/(?P<pkr>\d+)/document/(?P<pk>\d+)/$',
            views.DocumentDetail.as_view(), name='document_detail'),

    # 创建文档
    re_path(r'^product/(?P<pk>\d+)/document/create/$',
            views.DocumentCreate.as_view(), name='document_create'),

    # 修改文档
    re_path(r'^product/(?P<pkr>\d+)/document/(?P<pk>\d+)/update/$',
            views.DocumentUpdate.as_view(), name='document_update'),

    # 文档搜索
    path('document/search/', views.document_search, name='document_search'),


    # Ajax搜索
    path('ajax/search/', views.doc_ajax_search, name='doc_ajax_search'),

]
