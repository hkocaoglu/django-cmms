from django.urls import path

# from .views import HomePageView, AboutPageView,WorkPageView,WorkDetailView,WorkCreateView,WorkListView
from .views import WorkListView, WorkDetailView,WorkTodayView, WorkCreateView, WorkUpdateView, WorkDeleteView
from .views import HomePageView,AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    # path("work/", WorkPageView.as_view(), name="work"),
    # path("<slug:slug>/", WorkDetailView.as_view(), name="work-detail"),
    # path("work/create/", WorkCreateView.as_view(), name="WorkCreateView"),
    # path("work/list/", WorkListView.as_view(), name="WorkListView"),
    
    path('works/', WorkListView.as_view(), name='Work_list'),
    path('works2/', WorkTodayView.as_view(), name='Work_list_today'),
    path('works/create/', WorkCreateView.as_view(), name='Work_create'),
    path('Works/<int:pk>/', WorkDetailView.as_view(), name='Work_detail'),
    path('Works/<int:pk>/update/', WorkUpdateView.as_view(), name='Work_update'),
    path('Works/<int:pk>/delete/', WorkDeleteView.as_view(), name='Work_delete')
]
