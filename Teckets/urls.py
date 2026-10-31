from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

routers = DefaultRouter()
routers.register(r"guesets", views.GuestViewsSet)
routers.register(r"moivies", views.MovieViewSet)
routers.register(r"reservations", views.ReservationViewSet)


urlpatterns = [
    path("list/tickat/", views.list_tickat, name="list_tickat"),
    path("tickat/detail/<int:pk>/", views.tickat_detail, name="tickat_detail"),
    path("list2/tickat/", views.list2_tickat.as_view(), name="list2_tickat"),
    path(
        "tickat/detail2/<int:pk>", views.tickat_detail2.as_view(), name="tickat_detail2"
    ),
    path("rest/viewsets/", include(routers.urls)),
    path("serch/movie/", views.serch_movie, name="serch_movie"),
    path("new/reservation/", views.new_reservation, name="new_reservation"),
]
