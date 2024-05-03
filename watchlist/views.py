# from django.shortcuts import render
# from watchlist.models import Movie
# from django.http import JsonResponse


# def movie_list(request):
#     """
#     Function: movie_list
#     Description: Returns a list of all movies in the database
#     Parameters: request (HttpRequest)
#     Returns: JsonResponse
#     """
#     movies = Movie.objects.all()
#     return JsonResponse({"movies": list(movies.values())})


# def movie_details(request, pk):
#     """
#     Function: movie_details
#     Description: Retrieves the details of a movie based on its primary key (pk).

#     Parameters:
#     - request (HttpRequest): The incoming request object.
#     - pk (int): The primary key of the movie to retrieve.

#     Returns:
#     - JsonResponse: A JSON response containing the movie details. The response includes the movie's name, description, and is_watched status.

#     Raises:
#     - DoesNotExist: If the movie with the given primary key does not exist.
#     """
#     movie = Movie.objects.get(pk=pk)
#     return JsonResponse(
#         {
#             "name": movie.name,
#             "description": movie.description,
#             "is_watched": movie.is_watched,
#         }
#     )
