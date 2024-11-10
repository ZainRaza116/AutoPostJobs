from PIL import Image
import os
from typing import List
from config import Config
from logger import Logger

class ImageProcessor:
    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.logger = logger
        os.makedirs(self.config.RESIZED_DIR, exist_ok=True)

    def resize_images(self) -> List[str]:
        """Resize images to standard size and return list of paths."""
        resized_paths = []
        
        if not os.path.exists(self.config.IMAGES_DIR):
            self.logger.warning(f"Images directory not found at {self.config.IMAGES_DIR}")
            return resized_paths

        for filename in os.listdir(self.config.IMAGES_DIR):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(self.config.IMAGES_DIR, filename)
                output_path = os.path.join(self.config.RESIZED_DIR, filename)
                
                try:
                    with Image.open(input_path) as img:
                        resized_img = img.resize(self.config.IMAGE_SIZE)
                        resized_img.save(output_path)
                        resized_paths.append(output_path)
                        self.logger.info(f"Successfully resized {filename}")
                except Exception as e:
                    self.logger.error(f"Error processing image {filename}: {e}")
                    
        return resized_paths