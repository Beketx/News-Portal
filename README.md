# News-Portal
Django SSR

20/2020
Tags
get_absolute_url

21/2020
Forms
**form.cleaned_data сам распаковывает по валю данные
form.as_p as_ul as_table
News.objects.create(**form.cleaned_data)
form = NewForm(request.POST) reques.Post это данные из браузера

22/2020
Forms 2.0

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Главная страница'
        return context


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    extra_context = {'title': 'Главная'}

  get_queryset

  def clean_title:

  re.match(pattern, string)