import requests
import os

def download_image(url) -> None:
    """This function downloads an image in the current working directory"""
    response = requests.get(url)
    img_dir = url[len("https://images.dog.ceo/breeds"):]

    os.makedirs(os.path.dirname(f'./dog_images/{img_dir}'), exist_ok=True)

    with open(f'./dog_images/{img_dir}', 'wb') as f:
        f.write(response.content)

def get_all_breeds() -> dict:
    """This function returns a dictionary with all breeds."""
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    #TODO: Check if the request worked, otherwise raise an exception
    if response.status_code != 200:
        # print(requests.status_code)
        raise requests.exceptions.RequestException(response.json().get("message"))
    resp_json = response.json()
    all_breeds = resp_json.get('message')
    return all_breeds

def get_random_image() -> str:
    """This function return the URL of a random image."""
    # Use the random image endpoint and return the URL of a random image
    response = requests.get(f'https://dog.ceo/api/breeds/image/random')
    # Check if the request worked, otherwise raise an exception
    if response.status_code != 200:
        raise requests.exceptions.RequestException(response.json().get("message"))

    resp_json = response.json()
    return resp_json.get('message')

def get_images_by_breed(breed) -> str:
    """This function uses the by breed endpoint and returns a list of all images of a breed"""
    #TODO: Implement this function using the by bread API
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    # print(url)
    response = requests.get(url)
    if response.status_code != 200:
        # print(response.status_code)
        raise requests.exceptions.RequestException(response.json().get("message"))
    # print("run")
    resp_json = response.json()
    return resp_json.get('message')
