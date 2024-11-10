import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    CHROME_BINARY: str = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    IMAGES_DIR: str = os.path.join(BASE_DIR, "images")
    RESIZED_DIR: str = os.path.join(BASE_DIR, "resized_images")
    EXCEL_FILE: str = "Lower 3rd treasure coast (530) Most updated (1) (1).xlsx"
    LOGIN_URL: str = "https://treasurecoastrestaurants.com/wp-admin/post-new.php?post_type=job_listing"
    USERNAME: str = "ty@tcoaststudios.com"
    PASSWORD: str = "Showcast2024!"
    DEFAULT_TIMEOUT: int = 10
    UPLOAD_DELAY: int = 2
    PAGE_LOAD_DELAY: int = 6
    IMAGE_SIZE: tuple = (400, 400)