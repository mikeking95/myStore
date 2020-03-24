from django.views.generic import TemplateView
from products.models import Product

class HomePageView(TemplateView):
    #shopbase.html    
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['featured_list'] = Product.objects.all()[:5]
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

class RecipesPageView(TemplateView):
    template_name = 'recipes.html'

class newPageView(TemplateView): 
    template_name = 'contact.html'

class AnimatedGrid(TemplateView):
    template_name = 'animated-grid.html'

