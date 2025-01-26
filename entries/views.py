from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Entry

class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Success Created!"

class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Success Updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Sucess Deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)