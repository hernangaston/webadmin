from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic.list import ListView

class UserListView(ListView):

    model = User
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context