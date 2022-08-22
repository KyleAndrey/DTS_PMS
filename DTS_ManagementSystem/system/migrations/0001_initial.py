# Generated by Django 4.0.5 on 2022-08-21 04:04

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessStyle',
            fields=[
                ('businessStyleID', models.AutoField(primary_key=True, serialize=False)),
                ('businessStyleName', models.CharField(max_length=255, null=True)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryID', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=255, null=True)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50, null=True, verbose_name='Company Name')),
                ('companyAddress', models.CharField(max_length=200, null=True, verbose_name='Company Address')),
                ('region', models.CharField(max_length=100, null=True, verbose_name='Region')),
                ('province', models.CharField(max_length=100, null=True, verbose_name='Province')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='City')),
                ('barangay', models.CharField(max_length=100, null=True, verbose_name='Barangay')),
                ('postalCode', models.CharField(max_length=5, null=True, verbose_name='Postal Code')),
                ('companyTIN', models.CharField(max_length=12, null=True, unique=True, verbose_name='Company TIN')),
                ('contactPerson', models.CharField(max_length=50, null=True, verbose_name='Contact Person')),
                ('contactNumber', models.CharField(max_length=12, null=True, verbose_name='Contact Number')),
                ('contactPosition', models.CharField(max_length=30, null=True, verbose_name='Contact Person Position')),
                ('is_inactive', models.BooleanField(default=False)),
                ('date_of_inactivity', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('businessStyle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.businessstyle', verbose_name='Business Style')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('contentID', models.AutoField(primary_key=True, serialize=False)),
                ('contentName', models.CharField(max_length=255, null=True)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=255, null=True)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FormalLetter',
            fields=[
                ('formalID', models.AutoField(primary_key=True, serialize=False)),
                ('formalStatus', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20, null=True)),
                ('formalSubj', models.CharField(max_length=20, null=True)),
                ('dateIssued', models.DateField(blank=True, null=True)),
                ('companyName', models.CharField(max_length=255, null=True)),
                ('companyAddress', models.CharField(max_length=20, null=True)),
                ('receiverName', models.CharField(max_length=20, null=True)),
                ('position', models.CharField(max_length=20, null=True)),
                ('body', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.TextField(max_length=255, null=True)),
                ('itemPrice', models.CharField(max_length=20, null=True)),
                ('itemType', models.CharField(choices=[('Product', 'Product'), ('Service', 'Service')], max_length=20, null=True, verbose_name='Type')),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('projectTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('projectTypeName', models.CharField(max_length=255, null=True)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuotationForm',
            fields=[
                ('quotationFormID', models.AutoField(primary_key=True, serialize=False)),
                ('quotationStatus', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20, null=True)),
                ('quotationSubj', models.CharField(max_length=20, null=True)),
                ('dateIssued', models.DateField(blank=True, null=True)),
                ('companyName', models.CharField(max_length=100, null=True)),
                ('companyAddress', models.CharField(max_length=255, null=True)),
                ('receiverName', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('contactNum', models.CharField(max_length=20, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('grandTotal', models.CharField(max_length=100, null=True)),
                ('deliveryTerms', models.CharField(max_length=100, null=True)),
                ('paymentTerms', models.CharField(max_length=100, null=True)),
                ('validityTerms', models.CharField(max_length=100, null=True)),
                ('warrantyTerms', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagID', models.AutoField(primary_key=True, serialize=False)),
                ('tagName', models.CharField(max_length=255, null=True)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=100, null=True, verbose_name='Task Name')),
                ('phaseName', models.CharField(choices=[('Obtain PO', 'Obtain PO'), ('Confirm PO', 'Confirm PO'), ('Delivery', 'Delivery'), ('Payment', 'Payment')], max_length=20, verbose_name='Phase')),
                ('has_file', models.BooleanField(default=False)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unitID', models.AutoField(primary_key=True, serialize=False)),
                ('unitName', models.CharField(max_length=255, null=True)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvForm',
            fields=[
                ('salesInvID', models.AutoField(primary_key=True, serialize=False)),
                ('salesInvStatus', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20, null=True)),
                ('dateIssued', models.DateField(blank=True, null=True)),
                ('terms', models.CharField(max_length=100, null=True)),
                ('mop', models.CharField(max_length=255, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('grandTotal', models.CharField(max_length=100, null=True)),
                ('clients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.client', verbose_name='Client')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectType', models.CharField(blank=True, max_length=20, null=True, verbose_name='Project Type')),
                ('projectName', models.CharField(max_length=50, null=True, verbose_name='Project Name')),
                ('projectPhase', models.CharField(default='Obtain PO', max_length=20, verbose_name='Project Phase')),
                ('projectStatus', models.CharField(blank=True, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Ongoing', max_length=20, verbose_name='Project Status')),
                ('paymentTerms', models.CharField(max_length=5, null=True, verbose_name='Payment Terms')),
                ('deliveryTerms', models.CharField(max_length=5, null=True, verbose_name='Delivery Terms')),
                ('poDeadline', models.DateField(blank=True, null=True)),
                ('projectStart', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('projectDeadline', models.DateField(blank=True, null=True)),
                ('is_inactive', models.BooleanField(default=False)),
                ('date_of_inactivity', models.DateTimeField(blank=True, null=True)),
                ('clients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.client', verbose_name='Client')),
            ],
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('fileID', models.AutoField(primary_key=True, serialize=False)),
                ('fileName', models.CharField(max_length=255, null=True)),
                ('filePath', models.FileField(upload_to='documents/')),
                ('fileCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('clientID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.client', verbose_name='Client ID')),
                ('fileCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.category', verbose_name='Category')),
                ('fileContent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.content', verbose_name='Content')),
                ('fileTag', models.ManyToManyField(to='system.tag', verbose_name='Tag')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryReceipt',
            fields=[
                ('deliveryRecID', models.AutoField(primary_key=True, serialize=False)),
                ('deliveryRecStatus', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20, null=True)),
                ('dateIssued', models.DateField(blank=True, null=True)),
                ('terms', models.CharField(max_length=100, null=True)),
                ('clients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.client', verbose_name='Client')),
            ],
        ),
        migrations.CreateModel(
            name='BillingInvForm',
            fields=[
                ('billingInvID', models.AutoField(primary_key=True, serialize=False)),
                ('billingInvStatus', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20, null=True)),
                ('dateIssued', models.DateField(blank=True, null=True)),
                ('terms', models.CharField(max_length=100, null=True)),
                ('jopoNum', models.CharField(max_length=255, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('grandTotal', models.CharField(max_length=100, null=True)),
                ('clients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.client', verbose_name='Client')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskFile', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('is_file_uploaded', models.BooleanField(default=False)),
                ('is_done', models.BooleanField(default=False)),
                ('fileCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('projectID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.project', verbose_name='Project')),
                ('taskID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.task', verbose_name='Task ID')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemQuantity', models.CharField(max_length=20, null=True)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('billingInvID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.billinginvform', verbose_name='Billing Invoice Form ID')),
                ('deliveryReceiptID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.deliveryreceipt', verbose_name='Delivery Receipt Form ID')),
                ('itemID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.item', verbose_name='Item ID')),
                ('quotationFormID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.quotationform', verbose_name='Quotation Form ID')),
                ('salesInvFormID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.salesinvform', verbose_name='Sales Invoice Form ID')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.unit', verbose_name='Unit')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('contactNumber', models.CharField(blank=True, default='', max_length=12, verbose_name='Contact Number')),
                ('accountType', models.CharField(blank=True, choices=[('Sales Staff', 'Sales Staff'), ('Administrator', 'Administrator'), ('Engineering Staff', 'Engineering Staff'), ('Proprietor: Verifier', 'Proprietor: Verifier'), ('Sales Staff: Encoder', 'Sales Staff: Encoder'), ('Financial Staff: Verifier', 'Financial Staff: Verifier')], default='', max_length=50, verbose_name='Account Type')),
                ('date_of_inactivity', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.department', verbose_name='Department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]