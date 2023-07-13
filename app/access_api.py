import requests

def get_player_data(player_name):
    player_url = f"https://www.balldontlie.io/api/v1/players?search={player_name}"
    response = requests.get(player_url).json()
   
    if len(response['data']) == 0:
        return None
    player_data = response['data'][0]
    player_data['name'] = player_data['first_name'] + " " + player_data['last_name']
    player_data['image_url'] = get_player_image(player_data['name'])
    player_id = player_data['id']
    stats_url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}"
    response = requests.get(stats_url).json()
    if len(response['data']) > 0:
        stats_data = response['data'][0]
        player_data['stats'] = stats_data
    else:
        player_data['stats'] = None
    return player_data


def get_player_image(player_name):
    search_url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": f"{player_name} NBA player",
        "cx": '52187a0e8b53c4227',
        "key": 'AIzaSyBBf4Z3zjeoKXW4seQMcjg548pon1bajkM',
        "num": 1,  # Number of search results to retrieve (in this case, 1)
        "searchType": "image"  # Search type set to images
    }
    response = requests.get(search_url, params=params).json()

    if "items" in response:
        # Extract the image source (link) from the search result
        image_src = response["items"][0]["link"]
        return image_src

    return None