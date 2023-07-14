from app.app import app,db #imports flask app object
from app.access_api import get_player_data
import unittest,sys
sys.path.append('../project2') # imports python file from parent directory
from app.models import Favplayer


class SportsAPITest(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    #for seaching player data
    def test_get_player_data(self):
        # Valid data
        lebron_stats = {
            "games_played": 56,
            "player_id": 237,
            "season": 2022,
            "min": "35:42",
            "fgm": 11.09,
            "fga": 22.14,
            "fg3m": 2.21,
            "fg3a": 6.84,
            "ftm": 4.54,
            "fta": 5.89,
            "oreb": 1.18,
            "dreb": 7.16,
            "reb": 8.34,
            "ast": 6.8,
            "stl": 0.91,
            "blk": 0.61,
            "turnover": 3.27,
            "pf": 1.66,
            "pts": 28.93,
            "fg_pct": 0.501,
            "fg3_pct": 0.324,
            "ft_pct": 0.77
        }

        # No current stats
        steve_kerr = {}

        self.assertEqual(get_player_data('Lebron James')['stats'], lebron_stats)
        self.assertEqual(get_player_data('Steve kerr')['stats'], None)

    #loading main page
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    #loading favorites page
    def test_fav_page(self):
        response = self.app.get('/view_fav', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_addfavs_db(self):
        #adds a user to database
        response = self.app.post('/add', player={'player_id': '237',
                                    'player_name':'Lebron James',
                                    'team_name': 'Los Angeles Laker'})
        self.assertEqual(response.status_code, 302)  # Check that the response is a redirect
    
        #Query the database to check if the user was added
        player = Favplayer.query.filter_by(player_name='Lebron James').first()
        self.assertIsNotNone(player)  # Check that the player exists in the database

    
    #def test_comments_database(self):

    #def test_comments_limits(self):

if __name__ == '__main__':
    unittest.main()
