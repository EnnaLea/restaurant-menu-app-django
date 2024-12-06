from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["meals"] = MEAL_TYPE

        return context_data



class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
