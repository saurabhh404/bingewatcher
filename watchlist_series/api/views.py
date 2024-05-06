import traceback
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_series.models import Series
from watchlist_series.api.serializers import SeriesSerializer


@api_view(["GET", "POST"])
def entire_list(request):
    try:
        if request.method == "GET":
            series = Series.objects.all()
            serializer = SeriesSerializer(series, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "POST":
            serializer = SeriesSerializer(data=request.data)
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


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def series_details(request, pk):
    try:
        series = Series.objects.get(pk=pk)
        if request.method == "GET":
            serializer = SeriesSerializer(series, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "PUT":
            serializer = SeriesSerializer(series, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PATCH':
            serializer = SeriesSerializer(series, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == "DELETE":
            series.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Series.DoesNotExist:
        return Response(
            {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as ex:
        traceback.print_exc()
        return Response(
            {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
