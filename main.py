from parse import parse_new
from mail import send_mail


with open('last_movie.txt', 'a+', encoding="utf-8") as last_movie_file:
    last_movie = last_movie_file.readline()
    movies = parse_new(last_movie)
    last_movie_file.truncate(0)  # erase all text in file
    last_movie = movies[0].get("title")
    last_movie_file.write(last_movie)
recipients = []
try:
    import local_settings
    recipients = local_settings.recipients
except ModuleNotFoundError:
    with open('recipients.txt') as recipients_file:
        for line in recipients_file:
            line = line.split('#', 1)[0].strip()
            if not line:
                continue
            recipients.append(line)

send_mail(movies, recipients)
