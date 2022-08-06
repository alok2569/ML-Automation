from django.urls import path, re_path, include
# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'api', views.MlwebView, 'mlweb')
urlpatterns = [
    # path('', include(router.urls)),
    path('api', views.MlwebView, name="Mlweb"),
    path('csv', views.CsvView, name="CSV"),
    path('csvDetails/<int:pk>', views.CsvDetailView, name="csvDetails"),
]