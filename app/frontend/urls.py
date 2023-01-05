from django.urls import re_path
from frontend.views.homepage import HomepageView

urlpatterns = [
    re_path(r'^$', HomepageView.as_view(
        template_name='homepage.html',
    ), name='homepage'),
]
