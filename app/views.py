from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from app.models import User


# class IndexView(ListView):
#     paginate_by = 6
#     queryset = User.objects.order_by('-id')
#     context_object_name = 'users'
#     model = User
#     template_name = 'app/index.html'
#
#
#     def get_queryset(self):
#         query = self.request.GET.get('query')
#         if query:
#             return User.objects.filter(Q(fullname__icontains=query) |
#                                        Q(job__icontains=query) |
#                                        Q(address__icontains=query))
#         return User.objects.all()


def index(request):
    users = User.objects.all()
    query = request.GET.get("query")
    paginator = Paginator(users, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if query:
        users = users.filter(Q(fullname__icontains=query)
                             | Q(job__icontains=query)
                             | Q(address__icontains=query))
    else:
        users = User.objects.all()
    context = {
        'users':users,
        'query':query,
        'page_obj':page_obj
    }
    return render(request, 'app/index.html', context)

