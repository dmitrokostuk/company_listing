from django import forms


from .models import Company


class Company_Add_Form(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "company_name",
            "parent",
            "company_estimated_earnings",
            "content",

        ]