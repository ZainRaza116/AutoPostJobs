import json
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from typing import Dict, Any
from config import Config
from logger import Logger

class RestaurantUploader:
    def __init__(self, driver: webdriver.Chrome, config: Config, logger: Logger):
        self.driver = driver
        self.config = config
        self.logger = logger
        self.wait = WebDriverWait(self.driver, self.config.DEFAULT_TIMEOUT)

    def login(self) -> None:
        """Handle login process."""
        try:
            login_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Log in with username and password']"))
            )
            login_link.click()

            user_login = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='user_login']"))
            )
            user_login.send_keys(self.config.USERNAME)

            user_pass = self.driver.find_element(By.XPATH, "//input[@id='user_pass']")
            user_pass.send_keys(self.config.PASSWORD)

            submit_button = self.driver.find_element(By.XPATH, "//input[@id='wp-submit']")
            submit_button.click()
            
            self.logger.info("Successfully logged in")
        except TimeoutException:
            self.logger.warning("Login elements not found, continuing without login")

    def upload_restaurant(self, row: pd.Series, image_paths: List[str]) -> None:
        """Handle the upload process for a single restaurant."""
        try:
            self._fill_basic_info(row)
            self._handle_categories(row)
            self._upload_images(image_paths)
            self._handle_business_hours(row)
            self._handle_amenities(row)
            self._fill_contact_info(row)
            self._publish_listing()
            
            self.logger.info(f"Successfully uploaded restaurant: {row['name']}")
        except Exception as e:
            self.logger.error(f"Error uploading restaurant {row['name']}: {e}")