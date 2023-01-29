from django.urls import path
from .views import stude_get,student_post,student_delete,student_update,index

urlpatterns = [
    path('',index),
    path('get/', stude_get),
    path('post/' , student_post),
    path('put/<int:id>/' , student_update),
    path('delete/<int:id>/' , student_delete),
]