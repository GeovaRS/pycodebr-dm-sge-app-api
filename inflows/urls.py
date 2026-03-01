from django.urls import path
from . import views


urlpatterns = [
    path(
        'inflows/list/',
        views.InFlowListView.as_view(),
        name='inflow_list',
    ),
    path(
        'inflows/create/',
        views.InFlowCreateView.as_view(),
        name='inflow_create',
    ),
    path(
        'inflows/<int:pk>/detail/',
        views.InFlowDetailView.as_view(),
        name='inflow_detail',
    ),
    path(
        'api/v1/inflows/',
        views.InFlowCreatListAPIView.as_view(),
        name='inflow-create-list-api-view'
    ),
    path(
        'api/v1/inflows/<int:pk>/',
        views.InFlowRetrieveAPIView.as_view(),
        name='inflow-detail-api-view'
    ),
]
