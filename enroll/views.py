from django.shortcuts import render
from enroll.forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.
# view function for redirecting the success page
def successpage(request):
    return render(request,"enroll/success.html")

def student_registration_detail(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Form Validated")
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            pasword = fm.cleaned_data['password']
            print(name)
            print(email)
            print(pasword)
            return HttpResponseRedirect('/regis/success/')

            #return render(request, "enroll/success.html",{'name':name,'email':email,'password':pasword})
    else:
        
        fm = StudentRegistration()
    return render(request, "enroll/studentlist.html",{'form':fm})

