from django.urls import path
from .import views 

urlpatterns = [
    path('',views.ProjectList, name="ProjectList"),
    path('createView', views.create_view , name = 'createView' ),
    path('<id>', views.detail_view ),
    path('updateView/<id>' , views.update_view , name= "update_view"),
    path('deleteView/<id>', views.delete_view , name="delete_view" ),
 ]