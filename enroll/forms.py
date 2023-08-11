from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    #This method is used to do cleaning and do custom validation on specified field apart from what django 
    #gives validation 
    # def clean_name(self):
    #     varname=self.cleaned_data['name']
    #     print(type(varname))
    #     if len(varname) < 4:
    #         raise forms.ValidationError("Please enter the text more than 4 character")
    #     elif not varname.isalpha():
    #         raise forms.ValidationError("Given name is should contain only alphabets")
        
    #     else:
    #         return varname
    
    def clean(self):
        self.cleaned_data = super().clean()
        varname = self.cleaned_data['name']
        varemail = self.cleaned_data['email']
        varpass = self.cleaned_data['password']
        print(type(varpass))
        
        #Custom validation for "name" field
        if len(varname) < 4:
             raise forms.ValidationError("Please enter the text more than 4 character")
        elif not varname.isalpha():
             raise forms.ValidationError("Given name is should contain only alphabets")
         
        #Custom validation for email field
        if len(varemail) < 10:
            raise forms.ValidationError("Email should be greater than 10")
        elif len(varemail) > 10:
              for i in varemail:
                  if i in ['_','/']:
                      raise forms.ValidationError("Email should not contain underscore(_) or slash(/) ")
                  
                  
                  
                  
        #Custom validation for password
        if len(varpass) < 8:
            raise forms.ValidationError("Password is too weak")
        elif ( varpass.isalpha() or varpass.isdigit()):
            raise forms.ValidationError("Passoword must contain alphabets and numerics")