from django.contrib import admin
from django.urls import path, include

import core.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls', namespace='recipes')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", core.views.HomePageView.as_view(), name="homepage"),
]