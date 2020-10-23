from django.urls import path
from news.views import ViewNews, CreateNews, HomeNews, NewsByCategory

urlpatterns = [
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('category/<int:category_id>/', NewsByCategory.as_view(extra_content={'title': 'Какой то тайтл'}),
    #      name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('', HomeNews.as_view(), name='home'),
]