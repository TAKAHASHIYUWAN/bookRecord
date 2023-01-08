from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BookCreate,BookDetail,BookList,BookDelete,BookListLogin,BookUpdate,RegistorBookRecordApp,BookPrice
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',BookList.as_view(),name='books'),
    path('detail-book/<int:pk>',BookDetail.as_view(),name='detail-book'),
    path('price-book/<int:pk>',BookPrice.as_view(),name='price-book'),
    path('create-book/',BookCreate.as_view(),name='create-book'),
    path('update-book/<int:pk>',BookUpdate.as_view(),name='update-book'),
    path('delete-book/<int:pk>',BookDelete.as_view(),name='delete-book'),
    path('login/',BookListLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'),
    path('register/',RegistorBookRecordApp.as_view(),name='register'),

    # nameはurl に簡易的にアクセスできるようにするもの
    # nameはhtmlでurlを使うときに
]   

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

"""
urlpatterns = [
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
"""