import requests
import http.client


import requests

def search_player(player_name):
    player_url = f"https://www.balldontlie.io/api/v1/players?search={player_name}"
    response = requests.get(player_url)
   
    if response.status_code == 200:
        player_data = response.json()['data'][0]
        player_id = player_data['id']
        stats_url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}"
        response = requests.get(stats_url).json()
        stats_data = response['data'][0]
        player_data.update(stats_data)
        return player_data
    else:
        print("Error: Failed to retrieve player data.")
        return None

# Example usage
player_name = input("Enter player name: ")
player_data = search_player("Lebron")

if player_data is not None:
    print(player_data)





