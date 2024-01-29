from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import UserModel


class UserCreationForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email", "password"]
        widgets = {
            "first_name": TextInput(attrs={"class":"form-control"}),
            "last_name": TextInput(attrs={"class":"form-control"}),
            "email": EmailInput(attrs={"class":"form-control"}),
            "password": PasswordInput(attrs={"class":"form-control"}), 
        }
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
