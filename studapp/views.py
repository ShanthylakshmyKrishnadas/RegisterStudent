from django.shortcuts import render,redirect
from studapp.models import registerStudent
# Create your views here.
def registerstudents(request):
    return render(request,'registerstudent.html')

def add_student_details(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        ph=request.POST['phone_number']
        em=request.POST['email']
        crse=request.POST['course']
        addr=request.POST['address']
        image=request.FILES.get('file')


        student=registerStudent(first_name=fname,
                               last_name=lname,
                               phone_number=ph,
                               email=em,
                               course=crse,
                               address=addr,
                               image=image)
        student.save()
        return redirect('show')
    
def show(request):
    students=registerStudent.objects.all()
    return render(request,'showstudent.html',{'student':students})

def studentprofile(request,sk):
    students=registerStudent.objects.get(id=sk)
    return render(request,'studentprofile.html',{'students':students})


def edit_student_profile(request,sk):
    if request.method=='POST':
        students=registerStudent.objects.get(id=sk)
        old=students.image
        new=request.FILES.get('file')
        if old !=None and new==None:
            students.image=old
        else:
            students.image=new
        students.first_name=request.POST.get('first_name')
        students.last_name=request.POST.get('last_name')
        students.phone_number=request.POST.get('phone_number')
        students.email=request.POST.get('email')
        students.course=request.POST.get('course')
        students.address=request.POST.get('address')
        students.save()
        return redirect('show')
    return render(request, 'studentprofile.html')

def deletepage(request,sk):
    students=registerStudent.objects.get(id=sk)
    return render(request,'delete.html',{'students':students})

#Deleting Product Element..
def delete_student(request,sk):
    students=registerStudent.objects.get(id=sk)
    students.delete()
    return redirect('show')
    