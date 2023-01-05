from django.shortcuts import render
from django.views import View


class HomepageView(View):
    initial = {'key': 'value'}
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})
