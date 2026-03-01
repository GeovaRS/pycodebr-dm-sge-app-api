from django.urls import path
from . import views


urlpatterns = [
    path(
        'outflows/list/',
        views.OutFlowListView.as_view(),
        name='outflow_list',
    ),
    path(
        'outflows/create/',
        views.OutFlowCreateView.as_view(),
        name='outflow_create',
    ),
    path(
        'outflows/<int:pk>/detail/',
        views.OutFlowDetailView.as_view(),
        name='outflow_detail',
    ),
    path(
        'api/v1/outflows/',
        views.OutFlowCreatListAPIView.as_view(),
        name='outflow-create-list-api-view'
    ),
    path(
        'api/v1/outflows/<int:pk>/',
        views.OutFlowRetrieveAPIView.as_view(),
        name='outflow-detail-api-view'
    ),
]
