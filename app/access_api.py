import requests

def get_player_data(player_name):
    player_url = f"https://www.balldontlie.io/api/v1/players?search={player_name}"
    response = requests.get(player_url).json()
   
    if len(response['data']) == 0:
        return None
    player_data = response['data'][0]
    player_data['name'] = player_data['first_name'] + " " + player_data['last_name']
    player_id = player_data['id']
    stats_url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}"
    response = requests.get(stats_url).json()
    if len(response['data']) > 0:
        stats_data = response['data'][0]
        player_data.update(stats_data)
    return player_data


