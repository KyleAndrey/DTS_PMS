from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import SetPasswordForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class CreateUser(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name', 'email', 'username']

		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Juan'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Dela Cruz'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g., juandelacruz@email.com'}),
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., juanDC'})
		}
	
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SetPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class departmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('departmentName', )

class businessStyleForm(forms.ModelForm):
    class Meta:
        model = BusinessStyle
        fields = ('businessStyleName', )

class projectTypeForm(forms.ModelForm):
    class Meta:
        model = ProjectType
        fields = ('projectTypeName', )

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskName', 'phaseName', 'has_file']

class unitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('unitName', )

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('categoryName', )

class contentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('contentName', )

class tagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tagName', )

class documentsForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['clientID', 'fileCategory', 'fileContent', 'fileTag', 'fileName', 'filePath']
    
    def __init__(self, *args, **kwargs):
        super(documentsForm, self).__init__(*args, **kwargs)

        self.fields['fileTag'].widget = forms.CheckboxSelectMultiple()
        self.fields['fileTag'].queryset = Tag.objects.all()

class itemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['itemName', 'itemPrice', 'itemType']
