from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .forms import NoteForm
from .models import NoteTable
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def redirect_to_index(request):
    return redirect("myapp:index")


class NoteIndexView(ListView):
    template_name = "index.html"
    model = NoteTable
    ordering = "-updated_at"


class NoteCreateView(CreateView):
    template_name = "note_input.html"
    form_class = NoteForm
    success_url = reverse_lazy("myapp:index")

    def form_valid(self, form):
        note = form.save(commit=False)
        note.updated_at = timezone.now()
        note.save()
        messages.success(self.request, "sucessful: 作成しました。")
        return super().form_valid(form)


class NoteDetailView(DetailView):
    template_name = "note_detail.html"
    model = NoteTable


class NoteUpdateView(UpdateView):
    template_name = "note_update.html"
    model = NoteTable
    fields = ("title", "text")
    success_url = reverse_lazy("myapp:index")

    def form_valid(self, form):
        note = form.save(commit=False)
        note.updated_at = timezone.now()
        note.save()
        messages.success(self.request, "sucessful: 更新しました。")
        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    template_name = "note_delete.html"
    model = NoteTable
    success_url = reverse_lazy("myapp:index")

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, "warn: 削除しました。")
        return super().delete(request, *args, **kwargs)
