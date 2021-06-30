from django import  forms
class Front(forms.Form):
    first_name = forms.CharField(max_length=20)
    middle_name = forms.CharField(max_length=10,required=False)
    last_name = forms.CharField(max_length=10)
    dob = forms.DateField(input_formats='%Y-%m-%d')
    gender = forms.ChoiceField(choices=(('male' , 'Male'),('female' , 'Female')))
    nationality = forms.ChoiceField(choices=(('Indian' , 'Indian'),('American', 'American'),('Others','Others')))
    city = forms.CharField(max_length=15)
    state = forms.CharField(max_length=15)
    pin_code = forms.IntegerField(max_value=699999,min_value=600000)
    qualification = forms.CharField(max_length=15)
    salary = forms.IntegerField(max_value=200000,min_value=0)
    pan = forms.CharField(max_length=10)