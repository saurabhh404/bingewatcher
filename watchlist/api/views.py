from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE", "PATCH"])
def movie_details(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)

        if request.method == "GET":
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method in ["PUT"]:
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == "PATCH":
            serializer = MovieSerializer(movie, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == "DELETE":
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Movie.DoesNotExist:
        return Response(
            {"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND
        )

    except Exception as ex:
        return Response(
            {"message": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
