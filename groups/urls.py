from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name="all"),
    path("new/", views.CreateGroup.as_view(), name="create"),
    path("posts/in/<slug>/",views.SingleGroup.as_view(),name="single"),
    path("join/<slug>/",views.JoinGroup.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveGroup.as_view(),name="leave"),
    path('group/<slug>/publish/', views.group_publish, name='group_publish'),
    path('delete/<int:pk>/', views.SchoolDeleteView, name='group_delete'),
    path('drafts/', views.DraftListView.as_view(), name='draft_group'),
    
    
]
