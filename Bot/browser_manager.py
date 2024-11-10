import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config
from logger import Logger

class BrowserManager:
    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.logger = logger

    def kill_chrome_processes(self) -> bool:
        """Kill any existing Chrome processes."""
        self.logger.info("Cleaning up Chrome processes...")
        try:
            subprocess.run(
                ['taskkill', '/F', '/IM', 'chrome.exe'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            subprocess.run(
                ['taskkill', '/F', '/IM', 'chromedriver.exe'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(f"Error killing Chrome processes: {e}")
            return False

    def initialize_driver(self) -> webdriver.Chrome:
        """Initialize and return Chrome WebDriver with configured options."""
        chrome_options = Options()
        chrome_options.binary_location = self.config.CHROME_BINARY
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        return webdriver.Chrome(options=chrome_options)