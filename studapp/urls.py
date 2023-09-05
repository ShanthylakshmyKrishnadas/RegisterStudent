from studapp import views
from django.urls import path

urlpatterns = [
    path('',views.registerstudents,name='registerstudents'),
    path('add_student_details',views.add_student_details,name='add_student_details'),
    path('show',views.show,name='show'),

    path('studentprofile/<int:sk>',views.studentprofile,name='studentprofile'),
    path('deletepage/<int:sk>',views.deletepage,name='deletepage'),
    path('edit_student_profile/<int:sk>',views.edit_student_profile,name='edit_student_profile'),
    path('delete_student/<int:sk>',views.delete_student,name='delete_student')
]
