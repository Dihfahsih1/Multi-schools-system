from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('canon/', include('schools.urls')),
    # # Third party apps here
    # url(r'^comments/', include('django_comments.urls')),
    # # url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    # url(r'^markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
