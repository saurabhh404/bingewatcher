import traceback

from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist.api.permissions import AdminOrReadOnly
from watchlist.api.permissions import ReviewUserOrReadOnly
from watchlist.api.serializers import ReviewSerializer
from watchlist.api.serializers import StreamPlatformSerializer
from watchlist.api.serializers import WatchlistSerializer
from watchlist.models import Review
from watchlist.models import StreamPlatform
from watchlist.models import Watchlist


class WatchlistListView(APIView):
    permission_classes = [AdminOrReadOnly]

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
                if Watchlist.objects.filter(
                    title=serializer.validated_data["title"]
                ).exists():
                    return Response(
                        {"message": "Watchlist with this title already exists"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
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
    permission_classes = [AdminOrReadOnly]

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
    permission_classes = [AdminOrReadOnly]

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

    def perform_update(self, serializer):
        pk = self.kwargs["pk"]
        try:
            review_item = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise ValidationError(
                {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
            )

        watchlist_item = Watchlist.objects.get(pk=review_item.watchlist.pk)
        # print("[prev]watchlist_item.sum_of_ratings: ", watchlist_item.sum_of_ratings)

        watchlist_item.sum_of_ratings = (
            watchlist_item.sum_of_ratings
            - review_item.rating
            + serializer.validated_data["rating"]
        )
        # print("review_item.rating: ", review_item.rating)
        # print(
        #     "serializer.validated_data['rating']: ", serializer.validated_data["rating"]
        # )
        # print("watchlist_item.sum_of_ratings: ", watchlist_item.sum_of_ratings)
        # print("[prev]watchlist_item.avg_rating: ", watchlist_item.avg_rating)
        # print(
        #     "[prev]watchlist_item.number_of_ratings: ", watchlist_item.number_of_ratings
        # )

        watchlist_item.avg_rating = (
            watchlist_item.sum_of_ratings / watchlist_item.number_of_ratings
        )
        # print("watchlist_item.avg_rating: ", watchlist_item.avg_rating)

        watchlist_item.save()
        serializer.save(watchlist=watchlist_item)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        item = Watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(review_user=review_user, watchlist=item)
        if review_queryset.exists():
            raise ValidationError({"message": "You have already reviewed this item"})

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
