from django.urls import path,re_path


from . import views

app_name="polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("chat",views.chatPage,name="chat_page"),
    path("<int:film_id>/", views.descriptionView,name="description"),
    path("form", views.get_name, name="form"),
    path("contact", views.contact, name="contact"),
    path("async",views.async_view, name="async"),
    path("sync", views.sync_view, name="sync"),
    path("profile/<user_username>",views.ProfileView,name="profile"),
    path("watchlist/<int:watchlist_id>",views.WatchlistView.as_view(), name="watchlist"),
    path('<int:film_id>/2', views.like_film, name="like"),
    path('<int:film_id>/3', views.watchlist_film, name="adding"),
    path("search",views.search, name="search"),
    path("popular/",views.popularView.as_view(),name="popular"),
    path("classic/",views.classicView.as_view(),name="classic"),
    path("trend/",views.trendView.as_view(),name="trend"),
    path("unseen/",views.unseenView.as_view(),name="unseen"),
    path("about/",views.aboutView,name="about")
]
#urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
