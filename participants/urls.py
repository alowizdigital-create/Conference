from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.participant_list,
        name='participant_list'
    ),

    path(
        'create/',
        views.participant_create,
        name='participant_create'
    ),
        
    path(
        'edit/<uuid:uuid>/',
        views.participant_update,
        name='participant_update'
    ),

    path(
        'delete/<uuid:uuid>/',
        views.participant_delete,
        name='participant_delete'
    ),

     path(
        "dashboard",
        views.dashboard,
        name="dashboard"
    ),

]
