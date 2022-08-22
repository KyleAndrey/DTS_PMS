from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

now = timezone.now
formStatus = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved')
]

class Department(models.Model):
    departmentName = models.CharField(max_length=255, null=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' %(self.departmentName)

class CustomUser(AbstractUser):
    type = [
        ('Sales Staff', 'Sales Staff'),
        ('Administrator', 'Administrator'),
        ('Engineering Staff', 'Engineering Staff'),
        ('Proprietor: Verifier', 'Proprietor: Verifier'),
        ('Sales Staff: Encoder', 'Sales Staff: Encoder'),
        ('Financial Staff: Verifier', 'Financial Staff: Verifier')
    ]
    department = models.ForeignKey(Department, verbose_name="Department", blank=True, null=True, on_delete=models.SET_NULL)
    contactNumber = models.CharField(max_length=12, verbose_name="Contact Number", blank=True, default='')
    accountType = models.CharField(choices=type, max_length=50, verbose_name="Account Type", blank=True, default='')
    date_of_inactivity = models.DateTimeField(blank=True, null=True)

class BusinessStyle(models.Model):
    businessStyleID =  models.AutoField(primary_key=True)
    businessStyleName = models.CharField(max_length=255, null=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' %(self.businessStyleName)

class Client(models.Model):
    businessStyle = models.ForeignKey(BusinessStyle, verbose_name='Business Style', null=True, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50, verbose_name="Company Name", null=True)
    companyAddress = models.CharField(max_length=200, verbose_name="Company Address", null=True)
    region = models.CharField(max_length=100, verbose_name="Region", null=True)
    province = models.CharField(max_length=100, verbose_name="Province", null=True)
    city = models.CharField(max_length=100, verbose_name="City", null=True)
    barangay = models.CharField(max_length=100, verbose_name="Barangay", null=True)
    postalCode = models.CharField(max_length=5, verbose_name="Postal Code", null=True)
    companyTIN = models.CharField(max_length=12, verbose_name="Company TIN", unique=True, null=True)
    contactPerson = models.CharField(max_length=50, verbose_name="Contact Person", null=True)
    contactNumber = models.CharField(max_length=12, verbose_name="Contact Number", null=True)
    contactPosition = models.CharField(max_length=30, verbose_name="Contact Person Position", null=True)
    is_inactive = models.BooleanField(default=False)
    date_of_inactivity = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return '[%s] %s' %(self.companyTIN, self.companyName)

class ProjectType(models.Model):
    projectTypeID =  models.AutoField(primary_key=True)
    projectTypeName = models.CharField(max_length=255, null=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' %(self.projectTypeName)

class Project(models.Model):
    status = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ]
    clients = models.ForeignKey(Client, verbose_name="Client", null=True, on_delete=models.CASCADE)
    projectType = models.CharField(max_length=20, verbose_name="Project Type", null=True, blank=True)
    projectName = models.CharField(max_length=50, verbose_name="Project Name", null=True)
    projectPhase = models.CharField(max_length=20, verbose_name="Project Phase", default='Obtain PO')
    projectStatus = models.CharField(choices=status, max_length=20, verbose_name="Project Status", blank=True, default='Ongoing')
    paymentTerms = models.CharField(max_length=5, verbose_name="Payment Terms", null=True)
    deliveryTerms = models.CharField(max_length=5, verbose_name="Delivery Terms", null=True)
    poDeadline = models.DateField(blank=True, null=True)
    projectStart = models.DateField(blank=True, default=now)
    projectDeadline = models.DateField(blank=True, null=True)
    is_inactive = models.BooleanField(default=False)
    date_of_inactivity = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '[%s] %s' %(self.projectName, self.clients.companyName)

class Task(models.Model):
    phase = [
        ('Obtain PO', 'Obtain PO'),
        ('Confirm PO', 'Confirm PO'),
        ('Delivery', 'Delivery'),
        ('Payment', 'Payment'),
    ]
    taskName = models.CharField(max_length=100, verbose_name="Task Name", null=True)
    phaseName = models.CharField(choices=phase, max_length=20, verbose_name="Phase")
    has_file = models.BooleanField(default=False)
    is_inactive = models.BooleanField(default=False)
    
    def __str__(self):
        return '[%s] %s' %(self.phaseName, self.taskName)

class AssignedTask(models.Model):
    taskID = models.ForeignKey(Task, verbose_name="Task ID", null=True, on_delete=models.CASCADE)
    projectID = models.ForeignKey(Project, verbose_name="Project", null=True, on_delete=models.CASCADE)
    taskFile = models.FileField(upload_to='documents/', blank=True, null=True)
    is_file_uploaded = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    fileCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[%s]' %(self.id)

class Unit(models.Model):
    unitID =  models.AutoField(primary_key=True)
    unitName = models.CharField(max_length=255, null=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' %(self.unitName)

class Category(models.Model):
    categoryID =  models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=255, null=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' %(self.categoryName)

class Content(models.Model):
    contentID =  models.AutoField(primary_key=True)
    contentName = models.CharField(max_length=255, null=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' %(self.contentName)

class Tag(models.Model):
    tagID =  models.AutoField(primary_key=True)
    tagName = models.CharField(max_length=255, null=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' %(self.tagName)

class FileModel(models.Model):
    fileID =  models.AutoField(primary_key=True)
    clientID = models.ForeignKey(Client, verbose_name="Client ID", null=True, on_delete=models.CASCADE)
    fileCategory = models.ForeignKey(Category, verbose_name="Category", null=True, on_delete=models.CASCADE)
    fileContent = models.ForeignKey(Content, verbose_name="Content", null=True, on_delete=models.CASCADE)
    fileTag = models.ManyToManyField(Tag, verbose_name="Tag")
    fileName = models.CharField(max_length=255, null=True)
    filePath = models.FileField(upload_to='documents/')
    fileCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' %(self.fileName)    

class Item(models.Model):
    type = [
        ('Product', 'Product'),
        ('Service', 'Service'),
    ]
    itemID = models.AutoField(primary_key=True)
    itemName = models.TextField(max_length=255, null=True)
    itemPrice = models.CharField(max_length=20, null=True)
    itemType = models.CharField(choices=type, max_length=20, verbose_name="Type", null=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return '%s' %(self.itemName)

class FormalLetter(models.Model):
    formalID = models.AutoField(primary_key=True)
    formalStatus = models.CharField(choices=formStatus, default="Pending", max_length=20, null=True)
    formalSubj = models.CharField(max_length=20, null=True)
    dateIssued = models.DateField(blank=True, null=True)
    companyName = models.CharField(max_length=255, null=True)
    companyAddress = models.CharField(max_length=20, null=True)
    receiverName = models.CharField(max_length=20, null=True)
    position = models.CharField(max_length=20, null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return '[%s] %s' %(self.formalID, self.formalSubj)
    @property
    def formalLetterNumber(self):
        if self.pk:
            return "{}{:05d}".format('FLN-', self.pk)
        else:
            return ""

class QuotationForm(models.Model):
    quotationFormID = models.AutoField(primary_key=True)
    quotationStatus = models.CharField(choices=formStatus, default="Pending", max_length=20, null=True)
    quotationSubj = models.CharField(max_length=20, null=True)
    dateIssued = models.DateField(blank=True, null=True)
    companyName = models.CharField(max_length=100, null=True)
    companyAddress = models.CharField(max_length=255, null=True)
    receiverName = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    contactNum = models.CharField(max_length=20, null=True)
    total = models.CharField(max_length=100, null=True)
    grandTotal = models.CharField(max_length=100, null=True)
    deliveryTerms = models.CharField(max_length=100, null=True)
    paymentTerms = models.CharField(max_length=100, null=True)
    validityTerms = models.CharField(max_length=100, null=True)
    warrantyTerms = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '[%s] %s' %(self.quotationFormID, self.quotationSubj)
    @property
    def quotationFormNumber(self):
        if self.pk:
            return "{}{:05d}".format('QFN-', self.pk)
        else:
            return ""

class BillingInvForm(models.Model):
    billingInvID = models.AutoField(primary_key=True)
    clients = models.ForeignKey(Client, verbose_name="Client", null=True, on_delete=models.CASCADE)
    billingInvStatus = models.CharField(choices=formStatus, default="Pending", max_length=20, null=True)
    dateIssued = models.DateField(blank=True, null=True)
    terms = models.CharField(max_length=100, null=True)
    jopoNum = models.CharField(max_length=255, null=True)
    total = models.CharField(max_length=100, null=True)
    grandTotal = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '[%s]' %(self.billingInvID)
    @property
    def billingInvNumber(self):
        if self.pk:
            return "{}{:05d}".format('BIN-', self.pk)
        else:
            return ""
    
class SalesInvForm(models.Model):
    salesInvID = models.AutoField(primary_key=True)
    clients = models.ForeignKey(Client, verbose_name="Client", null=True, on_delete=models.CASCADE)
    salesInvStatus = models.CharField(choices=formStatus, default="Pending", max_length=20, null=True)
    dateIssued = models.DateField(blank=True, null=True)
    terms = models.CharField(max_length=100, null=True)
    mop = models.CharField(max_length=255, null=True)
    total = models.CharField(max_length=100, null=True)
    grandTotal = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '[%s]' %(self.salesInvID)
    @property
    def salesInvNumber(self):
        if self.pk:
            return "{}{:05d}".format('SIN-', self.pk)
        else:
            return ""

class DeliveryReceipt(models.Model):
    deliveryRecID = models.AutoField(primary_key=True)
    clients = models.ForeignKey(Client, verbose_name="Client", null=True, on_delete=models.CASCADE)
    deliveryRecStatus = models.CharField(choices=formStatus, default="Pending", max_length=20, null=True)
    dateIssued = models.DateField(blank=True, null=True)
    terms = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '[%s]' %(self.deliveryRecID)
    @property
    def deliveryRecNumber(self):
        if self.pk:
            return "{}{:05d}".format('DRN-', self.pk)
        else:
            return ""

class AssignedItem(models.Model):
    itemID = models.ForeignKey(Item, verbose_name="Item ID", null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, verbose_name="Unit", null=True, on_delete=models.CASCADE)
    quotationFormID = models.ForeignKey(QuotationForm, verbose_name="Quotation Form ID", null=True, on_delete=models.CASCADE)
    billingInvID = models.ForeignKey(BillingInvForm, verbose_name="Billing Invoice Form ID", null=True, on_delete=models.CASCADE)
    salesInvFormID = models.ForeignKey(SalesInvForm, verbose_name="Sales Invoice Form ID", null=True, on_delete=models.CASCADE)
    deliveryReceiptID = models.ForeignKey(DeliveryReceipt, verbose_name="Delivery Receipt Form ID", null=True, on_delete=models.CASCADE)
    itemQuantity = models.CharField(max_length=20, null=True)
    amount = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '[%s]' %(self.id)
