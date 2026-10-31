from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Guest, Movie, Reservation
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets


@api_view(["GET", "POST"])
def list_tickat(request):
    if request.method == "GET":
        guest = Guest.objects.all()
        serializer = GuestSerializer(guest, many=True)
        return Response(
            serializer.data,
        )
    elif request.method == "POST":
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.datd, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def tickat_detail(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        serializer = GuestSerializer(guest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class list2_tickat(APIView):
    def get(self, request):
        guest = Guest.objects.all()
        serializer = GuestSerializer(guest, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class tickat_detail2(APIView):
    def get(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GuestSerializer(guest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GuestViewsSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


@api_view(["GET"])
def serch_movie(request):
    movie = Movie.objects.filter(movie=request.data["movie"])
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def new_reservation(request):
    movie = Movie.objects.get(hall=request.data["hall"], movie=request.data["movie"])
    guest = Guest()
    guest.name = request.data["name"]
    guest.mobile = request.data["mobile"]
    guest.save()
    reservation = Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save()
    return Response(
        ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED
    )
