import datetime

from db.models import MovieSession


def create_movie_sessions(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )

def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date:
        parsed_date = datetime.date.strptime(session_date, '%Y-%m-%d')
        movie_sessions = movie_sessions.filter(show_time__date=parsed_date)
    return movie_sessions

def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)
