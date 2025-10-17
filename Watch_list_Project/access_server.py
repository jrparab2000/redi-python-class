import requests

def search_show(title):
    url = f"https://api.tvmaze.com/singlesearch/shows?q={title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Show not found on the data base or API not found")
        return None

def print_show_data(title):
    data = search_show(title)
    print(data)
    if data == None:
        return None
    
    per_movie = {}

    temp = data['summary']
    temp = temp.replace("</p>","")
    temp = temp.replace("<p>","")

    per_movie.update({"Title" : data ['name']})
    per_movie.update({"Genres" : data['genres']})
    per_movie.update({"Rating" : data['rating']['average']})
    per_movie.update({"Summary" : temp})
    per_movie.update({"Watched" : False})
    per_movie.update({"Review" : 0})

    
    print(f"Title: {data['name']}")
    print(f"Genres: {', '.join(data['genres'])}")
    print(f"Official Rating: {data['rating']['average']}")
    print(f"Summary: {temp}")
    return per_movie

