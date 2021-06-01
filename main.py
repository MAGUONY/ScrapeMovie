import requests
from bs4 import BeautifulSoup

URL = "http://web.archive.org/web/20200514054348/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

websiteHtml = response.text

soup = BeautifulSoup(websiteHtml, "html.parser")

allMovies = soup.find_all(name="h3", class_="title")

movieTitles = [movie.getText() for movie in allMovies]

movies = movieTitles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

print(movies)
