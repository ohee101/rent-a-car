from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from car.views import admin_car_list, admin_msg, order_list, car_created, order_update, order_delete, msg_delete
from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', admin_car_list, name='adminIndex'),
    url(r'^listOrder/$', order_list, name="order_list"),
    url(r'^(?P<id>\d+)/editOrder/$', order_update, name="order_edit"),
    url(r'^(?P<id>\d+)/deleteOrder/$', order_delete, name="order_delete"),
    url(r'^create/$', car_created, name="car_create"),
    url(r'^message/$', admin_msg, name='message'),
    url(r'^(?P<id>\d+)/deletemsg/$', msg_delete, name="msg_delete"),
    url(r'^car/', include('car.urls')),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
