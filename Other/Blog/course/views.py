from django.shortcuts import render
from django.views import View
# Create your views here.
class CourseView(View):
    template_name = "contact.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

def my_fbv(request, *args, **kwargs):
    return render(request, "Course/contact.html", {})