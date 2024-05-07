import traceback
from rest_framework import (
    status,
    generics,
)
from rest_framework.views import APIView
from rest_framework.response import Response

from watchlist.models import Watchlist, StreamPlatform, Review
from watchlist.api.serializers import (
    WatchlistSerializer,
    StreamPlatformSerializer,
    ReviewSerializer,
)


class WatchlistListView(APIView):
    def get(self, request):
        try:
            watch_item = Watchlist.objects.all()
            serializer = WatchlistSerializer(watch_item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            serializer = WatchlistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class WatchlistDetailsView(APIView):
    def get(self, request, pk):
        try:
            watch_item = Watchlist.objects.get(pk=pk)
            serializer = WatchlistSerializer(watch_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Watchlist.DoesNotExist:
            return Response(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk):
        try:
            watch_item = Watchlist.objects.get(pk=pk)
            serializer = WatchlistSerializer(watch_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Watchlist.DoesNotExist:
            return Response(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            watch_item = Watchlist.objects.get(pk=pk)
            watch_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Watchlist.DoesNotExist:
            return Response(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, pk):
        try:
            watch_item = Watchlist.objects.get(pk=pk)
            serializer = WatchlistSerializer(
                watch_item, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Watchlist.DoesNotExist:
            return Response(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class StreamPlatformListView(APIView):
    def get(self, request):
        try:
            stream_platform = StreamPlatform.objects.all()
            serializer = StreamPlatformSerializer(stream_platform, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            serializer = StreamPlatformSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class StreamPlatformDetailsView(APIView):
    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(stream_platform)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StreamPlatform.DoesNotExist:
            return Response(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(stream_platform, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StreamPlatform.DoesNotExist:
            return Response(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
            stream_platform.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StreamPlatform.DoesNotExist:
            return Response(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(
                stream_platform, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StreamPlatform.DoesNotExist:
            return Response(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            traceback.print_exc()
            return Response(
                {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        item = Watchlist.objects.get(pk=pk)
        serializer.save(watchlist=item)
