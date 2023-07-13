#grabbing API Data
from access_api import get_player_data

def test_get_player_data():
    #valid data
    lebron_stats = {"games_played":56,"player_id":236,"season":2022,
                    "min":"35:42","fgm":11.09,"fga":22.14,"fg3m":2.21,
                    "fg3a":6.84,"ftm":4.54,"fta":5.89,"oreb":1.18,"dreb":7.16,
                    "reb":8.34,"ast":6.8,"stl":0.91,"blk":0.61,"turnover":3.27,
                    "pf":1.66,"pts":28.93,"fg_pct":0.501,"fg3_pct":0.324,
                    "ft_pct":0.77}
    #no current stats
    steve_kerr = {}

    assert get_player_data('Lebron James') == lebron_stats
    assert get_player_data('Steve kerr') == None 


test_get_player_data()