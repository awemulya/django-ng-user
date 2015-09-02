
__author__ = 'awemulya'

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from subprocess import Popen, PIPE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class CygwinFirefoxProfile(FirefoxProfile):

    @property
    def path(self):

        path = self.profile_dir

        # cygwin requires to manually specify Firefox path a below:
        # PATH=/cygdrive/c/Program\ Files\ \(x86\)/Mozilla\ Firefox/:$PATH
        try:
            proc = Popen(['cygpath','-d',path], stdout=PIPE, stderr=PIPE)
            stdout, stderr = proc.communicate()
            path = stdout.split('\n', 1)[0]

        except OSError:
            print("No cygwin path found")

        return path


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        import os
        from selenium import webdriver

        # chromedriver = "/Users/adam/Downloads/chromedriver"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # firefoxProfile = CygwinFirefoxProfile()
        # ## Disable CSS
        # firefoxProfile.set_preference('permissions.default.stylesheet', 2)
        # ## Disable images
        # firefoxProfile.set_preference('permissions.default.image', 2)
        # ## Disable Flash
        # firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        # self.driver = webdriver.Firefox(firefoxProfile)
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:8000/register/"
        self.email = "awemulya@gmail.com"
        self.date = "09/02/2015"
        self.password = "123456"

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Registration Page", driver.title)
        date_of_birth = driver.find_element_by_name("date_of_birth")
        date_of_birth.send_keys(self.date)
        date_of_birth.send_keys(Keys.ESCAPE)
        # wait = WebDriverWait(driver, 10)
        # elems = driver.find_elements(By.XPATH,  "//input[contains(@class, 'date_of_birth')]")
        # element = wait.until(EC.element_to_be_clickable((By.ID,'date_of_birth')))
        # import pdb
        # pdb.set_trace()
        # driver.find_element_by_name("date_of_birth").click();
        # driver.find_element_by_name("next").click();
        # driver.find_element_by_name("28").click();
        # time.sleep(2)
        email = driver.find_element_by_name("email")
        email.send_keys(self.email)
        password1 = driver.find_element_by_name("password1")
        password1.send_keys(self.password)
        password2 = driver.find_element_by_name("password2")
        password2.send_keys(self.password)
        password2.send_keys(Keys.RETURN)
        assert "Registration Failed. Please try again." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
