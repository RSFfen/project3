from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): # new
    template_name = 'about.html'
    
class CarsPageView(TemplateView): # new
    template_name = 'cars.html'
    
class HelpPageView(TemplateView): # new
    template_name = 'help.html'
