from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    #USER
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),

    #HOME
    path('home/', views.home, name='home'),
    re_path(r'^$', RedirectView.as_view(pattern_name='home', permanent=False), name='index'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('userEditProfile/', views.userEditProfile, name='userEditProfile'),
    path('userPassword/', views.userPassword, name='userPassword'),
    
    #PROJECTS
    path('projects/', views.projects, name='projects'),
    path('newProject/', views.newProject, name='newProject'),
    path('projectOverview/1/', views.projectObtain, name='projectObtain'),
    path('projectOverview/2/', views.projectConfirm, name='projectConfirm'),
    path('projectOverview/3/', views.projectDelivery, name='projectDelivery'),
    path('projectOverview/4/', views.projectPayment, name='projectPayment'),

    #CLIENTS
    path('clients/', views.clients, name='clients'),
    path('newClient/', views.newClient, name='newClient'),
    path('clientProfile/', views.clientProfile, name='clientProfile'),
    path('editClient/', views.editClient, name='editClient'),

    #FORMS
    path('forms/', views.forms, name='forms'),
    path('quotationForm/', views.quotationForm, name='quotationForm'),
    path('quotationFormVerifier/', views.quotationFormVerifier, name='quotationFormVerifier'),
    path('quotationFormPDF/', views.quotationFormPDF, name='quotationFormPDF'),
    path('salesInvoiceForm/', views.salesInvoiceForm, name='salesInvoiceForm'),
    path('salesInvoiceFormVerifier/', views.salesInvoiceFormVerifier, name='salesInvoiceFormVerifier'),
    path('salesInvFormPDF/', views.salesInvFormPDF, name='salesInvFormPDF'),
    path('deliveryReceiptForm/', views.deliveryReceiptForm, name='deliveryReceiptForm'),
    path('deliveryReceiptFormVerifier/', views.deliveryReceiptFormVerifier, name='deliveryReceiptFormVerifier'),
    path('deliveryReceiptFormPDF/', views.deliveryReceiptFormPDF, name='deliveryReceiptFormPDF'),
    path('billingInvoiceForm/', views.billingInvoiceForm, name='billingInvoiceForm'),
    path('billingInvoiceFormVerifier/', views.billingInvoiceFormVerifier, name='billingInvoiceFormVerifier'),
    path('billingInvoiceFormPDF/', views.billingInvoiceFormPDF, name='billingInvoiceFormPDF'),
    path('formalLetterForm/', views.formalLetterForm, name='formalLetterForm'),
    path('formalLetterFormVerifier/', views.formalLetterFormVerifier, name='formalLetterFormVerifier'),
    path('formalLetterFormPDF/', views.formalLetterFormPDF, name='formalLetterFormPDF'),

    #DOCUMENTS
    path('documents/', views.documents, name='documents'),
    path('documentsClients/', views.documentsClients, name='documentsClients'),
    path('documentsFolder/', views.documentsFolder, name='documentsFolder'),
    path('documentsProjects/', views.documentsProjects, name='documentsProjects'),
    path('documentsCompanyReqs/', views.documentsCompanyReqs, name='documentsCompanyReqs'),
    path('documentsOthers/', views.documentsOthers, name='documentsOthers'),

    #REPORTS
    path('reports/', views.reports, name='reports'),
    path('reportsClients/', views.reportsClients, name='reportsClients'),
    path('reportsProducts/', views.reportsProducts, name='reportsProducts'),
    path('reportsServices/', views.reportsServices, name='reportsServices'),
    path('reportsBillingInvoice/', views.reportsBillingInvoice, name='reportsBillingInvoice'),
    path('reportsSalesInvoice/', views.reportsSalesInvoice, name='reportsSalesInvoice'),
    path('reportsDeliveryReceipt/', views.reportsDeliveryReceipt, name='reportsDeliveryReceipt'),
    path('reportsPDF/', views.reportsPDF, name='reportsPDF'),
    path('reportsClientsPDF/', views.reportsClientsPDF, name='reportsClientsPDF'),
    path('reportsProductsPDF/', views.reportsProductsPDF, name='reportsProductsPDF'),

    #ADMIN
    path('adminActiveClients/', views.adminActiveClients, name='adminActiveClients'),
    path('adminActiveProjects/', views.adminActiveProjects, name='adminActiveProjects'),
    path('adminActiveUsers/', views.adminActiveUsers, name='adminActiveUsers'),
    path('adminBusinessStyle/', views.adminBusinessStyle, name='adminBusinessStyle'),
    path('adminCategory/', views.adminCategory, name='adminCategory'),
    path('adminContent/', views.adminContent, name='adminContent'),
    path('adminDepartment/', views.adminDepartment, name='adminDepartment'),
    path('adminEditProfile/', views.adminEditProfile, name='adminEditProfile'),
    path('adminEditUser/', views.adminEditUser, name='adminEditUser'),
    path('adminHome/', views.adminHome, name='adminHome'),
    path('adminInactiveClients/', views.adminInactiveClients, name='adminInactiveClients'),
    path('adminInactiveProjects/', views.adminInactiveProjects, name='adminInactiveProjects'),
    path('adminInactiveUsers/', views.adminInactiveUsers, name='adminInactiveUsers'),
    path('adminPassword/', views.adminPassword, name='adminPassword'),
    path('adminProfile/', views.adminProfile, name='adminProfile'),
    path('adminProjectType/', views.adminProjectType, name='adminProjectType'),
    path('adminTag/', views.adminTag, name='adminTag'),
    path('adminTask/', views.adminTask, name='adminTask'),
    path('adminUnit/', views.adminUnit, name='adminUnit'),
    path('adminItem/', views.adminItem, name='adminItem'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)