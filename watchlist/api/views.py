import traceback
from rest_framework import (
    status,
    generics,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from watchlist.models import Watchlist, StreamPlatform, Review
from watchlist.api.serializers import (
    WatchlistSerializer,
    StreamPlatformSerializer,
    ReviewSerializer,
)
from watchlist.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly


class WatchlistListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [AdminOrReadOnly]

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
    permission_classes = [ReviewUserOrReadOnly]


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        item = Watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(review_user=review_user, watchlist=item)
        if review_queryset.exists():
            raise ValidationError(
                {"review_user": "You have already reviewed this item"}
            )

        if item.number_of_ratings == 0:
            item.avg_rating = serializer.validated_data["rating"]
            item.sum_of_ratings += serializer.validated_data["rating"]
            item.number_of_ratings += 1
        else:
            item.sum_of_ratings += serializer.validated_data["rating"]
            item.number_of_ratings += 1
            item.avg_rating = item.sum_of_ratings / item.number_of_ratings
        item.save()

        serializer.save(watchlist=item, review_user=review_user)
