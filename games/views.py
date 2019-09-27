from django.shortcuts import render
from .models import Game
from django.views.generic import DetailView, ListView
from django.db.models import F
from django.urls import reverse

def index(request):
    objects = Game.objects.all()
    objects = objects[:30]
    return render(request, 'gaming/index.html', {'objects':objects})


def Categories(request, cat):
    object_list = Game.objects.filter(category=cat)
    n = len(object_list)
    return render(request, 'gaming/cat.html', {"objects": object_list, "cat": cat, "n":n})

class GameDetailView(DetailView):
    model = Game
    template_name = 'gaming/game_detail.html'


    def get_success_url(self):
        return reverse("game_detail", kwargs={'pk':self.object.pk,'slug':self.object.slug})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = Game.objects.get(id=self.kwargs.get('pk'),slug=self.kwargs.get('slug'))
        cat = instance.category
        objects = Game.objects.filter(category=cat)
        context['objects'] = objects
        return context





class SearchResultsView(ListView):
    model = Game
    template_name = 'gaming/search_results.html'

    """def get_success_url(self):
        query = self.request.GET.get('q')
        item = Game.objects.get(title=query)
        return redirect("home")"""

    def get_queryset(self):
        query = self.request.GET.get('q')
        item = Game.objects.get(title=query)
        return item

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        item = Game.objects.get(title=query)
        objects = Game.objects.filter(category=item.category)
        context['objects'] = objects
        return context





          
