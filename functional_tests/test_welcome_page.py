import time
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from events.models import *


class TestWelcomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_request_login_page(self):
        self.browser.get('https://mycampusbackend.herokuapp.com/login/')
        # initial page request by user
        alert = self.browser.find_element_by_class_name('w3-display-middle')
        buttons = alert.find_elements_by_xpath("//button[@class='button']")
        login_button = True
        # check buttons show on page
        for button in buttons:
            if login_button:
                self.assertEqual(button.text, 'Log In')
            else:
                self.assertEqual(button.text, 'Sign Up')

            login_button = False
        print("Test request login page success")
    
    def test_buttons_perform_login_signup(self):
        self.browser.get('https://mycampusbackend.herokuapp.com/login/')
        # initial page request by user
        alert = self.browser.find_element_by_class_name('w3-display-middle')
        buttons = alert.find_elements_by_xpath("//button[@class='button']")
        login_button = True
        add_url = 'https://mycampusbackend.herokuapp.com' + reverse('signup')
        for button in buttons:
            if login_button:
                # check Log In button opens login modal
                button.click()
                self.assertEqual(
                    self.browser.find_element_by_id('id01').value_of_css_property('display'),
                    'block'
                )
                self.browser.find_element_by_id('id01').click()
            else:
                # check Sign Up button redirects to signup page
                button.click()
                self.assertEqual(
                    self.browser.current_url,
                    add_url
                )
            login_button = False
        print("Test buttons perform login and signup success")
    
    def test_invalid_login_username(self):
         self.browser.get('https://mycampusbackend.herokuapp.com/login/')

    def test_invalid_login_password(self):
        self.browser.get('https://mycampusbackend.herokuapp.com/login/')

    def test_invalid_signup_username(self):
        self.browser.get('https://mycampusbackend.herokuapp.com/signup/')

    def test_invalid_signup_password(self):
        self.browser.get('https://mycampusbackend.herokuapp.com/signup/')

    def test_invalid_signup_confirmation_password(self):
        self.browser.get('https://mycampusbackend.herokuapp.com/signup/')