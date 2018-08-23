from django.urls import include, path

urlpatterns = [
    path('api/user/', include('user.urls')),
    path('api/pipeline/', include('pipeline.urls')),
]
