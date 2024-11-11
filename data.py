import json


def get_films(file_path: str = 'data.json', film_id: int = None) -> list[dict] | dict:
    with open(file_path, 'r') as fp:
        films = json.load(fp)
        if film_id != None and film_id < len(films):
            return films[film_id]
        return films


