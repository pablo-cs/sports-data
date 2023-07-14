import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SystemTest (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')  # Replace with the URL of your Flask app
    
    def tearDown(self):
        self.driver.quit()
    
    def search_valid_curr_player_test(self):
        # Simulate searching for a player
        search_input = self.driver.find_element_by_name('search')
        search_input.send_keys('Lebron James')
        search_input.send_keys(Keys.RETURN)
        
        # Verify if the correct player information is displayed
        player_name = self.driver.find_element_by_id('name').text
        self.assertEqual(player_name, 'Lebron James')
        
        # Verify if the add to favorites button is displayed
        add_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Add to favorites')]")
        self.assertTrue(add_button.is_displayed())
        
        # Verify if the remove from favorites button is not displayed
        remove_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Remove from favorites')]")
        self.assertFalse(remove_button.is_displayed())
        

    def search_valid_noncurr_player_test(self):
        search_input = self.driver.find_element_by_name('search')
        search_input.send_keys('Michael Jordan')
        search_input.send_keys(Keys.RETURN)
        
        # Verify if the correct player information is displayed
        player_name = self.driver.find_element_by_id('name').text
        self.assertEqual(player_name, 'Michael Jordan')
        
        # Verify if the add to favorites button is displayed
        add_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Add to favorites')]")
        self.assertTrue(add_button.is_displayed())
        
        # Verify if the remove from favorites button is not displayed
        remove_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Remove from favorites')]")
        self.assertFalse(remove_button.is_displayed())
        
        # Verify if the Minutes stat is not present in the HTML
        minutes_th = self.driver.find_elements_by_xpath("//th[contains(text(), 'Minutes:')]")
        minutes_td = self.driver.find_elements_by_xpath("//td[@id='minutes']")
        self.assertEqual(len(minutes_th), 0)
        self.assertEqual(len(minutes_td), 0)


    def test_search_invalid_player(self):
        # Simulate searching for an invalid player
        search_input = self.driver.find_element_by_name('search')
        search_input.send_keys('Invalid Player')
        search_input.send_keys(Keys.RETURN)
        
        # Verify if the player not found message is displayed
        message = self.driver.find_element_by_xpath("//h2[contains(text(), 'Player Not Found')]")
        self.assertTrue(message.is_displayed())

if __name__ == '__main__':
    unittest.main()
