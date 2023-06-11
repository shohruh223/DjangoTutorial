from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext as _
from app.models import New


# class IndexView(TemplateView):
#     news = New.objects.order_by('-id')
#     template_name = 'app/index.html'


def index(request):
    text = _("So'ngi yangiliklar")
    news = New.objects.order_by('-id')
    return render(request, 'app/index.html', {"news":news, "text":text})


class CreateNew(CreateView):
    model = New
    fields = "__all__"
    template_name = 'app/new.html'

    def form_valid(self, form):
        result = super(CreateNew, self).form_valid(form)
        form.save()
        return result
