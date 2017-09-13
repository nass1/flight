from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name="findweb"

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name="mainpage"),

]
