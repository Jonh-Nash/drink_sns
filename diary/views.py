import logging
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, resolve_url

from django.urls import reverse_lazy
from django.views import generic
from .forms import InquiryForm, DiaryCreateForm, AccountsUpdateForm
from .models import Diary
from accounts import models


logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 5

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('created_at')
        return diaries


class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'


class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '投稿を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '投稿の作成に失敗しました。')
        return super().form_invalid(form)


class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('diary:diary_detail',
                            kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '投稿を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '投稿の更新に失敗しました。')
        return super().form_invalid(form)


class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_alllist')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '投稿を削除しました。')
        return super().delete(request, *args, **kwargs)


class DiaryAlllistView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 5
    diaries = Diary.objects.get


class UserOnlyMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class Profile(UserOnlyMixin, generic.DetailView):
    model = models.CustomUser
    template_name = 'pfofile.html'


class ProfileUpdate(UserOnlyMixin, generic.UpdateView):
    model = models.CustomUser
    form_class = AccountsUpdateForm
    template_name = 'pfofile_update.html'

    def get_success_url(self):
        return resolve_url('diary:profile', pk=self.kwargs['pk'])




