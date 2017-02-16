from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import sys
import unittest

MAX_WAIT = 5

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_meeting(self):
        # Sally hears about a website where she can create a meeting
        self.browser.get('http://localhost:8000')

        # She is presented with a page in which she can create a meeting
        meetingTitle = self.browser.find_element_by_id('meeting_title')
        startDate = self.browser.find_element_by_id('start_date')
        startTime = self.browser.find_element_by_id('start_time')
        duration = self.browser.find_element_by_id('duration')
        participants = self.browser.find_element_by_id('participants')
        agenda = self.browser.find_element_by_id('agenda')


        self.assertEqual(meetingTitle.get_attribute('placeholder'), 'Enter a name for your meeting')


        # She enters a meeting title into the meeting text box
        meetingTitle.send_keys('Test meeting 1')
        startDate.send_keys('3/30/2017')
        startTime.send_keys('')
        duration.send_keys('')
        participants.send_keys('')
        agenda.send_keys('')
        meetingTitle.send_keys(Keys.ENTER)

        # She is able to enter additional details such as date, time, and agenda items
        self.fail('Finish the test!')
        # Once the meeting is created, she is directed to a page with a custom URL for that meeting

        # The custom URL allows her to revisit this list whenever she likes.

        # Another user, Frank,  visits the site. He is invited to create a meeting.

        # Frank cannot see any information about Sally's meeting.

        # Frank's URL after creating the meeting is different than Sally's meeting URL.
