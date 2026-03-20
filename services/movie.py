from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] = None, actors: list[int] = None) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids and actors:
        movies = movies.filter(actors__id__in=actors, genres__id__in=genres_ids)
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors:
        movies = movies.filter(actors__id__in=actors)
    return movies

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)
