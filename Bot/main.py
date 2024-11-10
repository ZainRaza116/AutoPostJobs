import os
from config import Config
from logger import Logger
from image_processor import ImageProcessor
from browser_manager import BrowserManager
from restaurant_uploader import RestaurantUploader
import pandas as pd

def main():
    config = Config()
    logger = Logger("restaurant_automation", "automation")

    os.makedirs("logs", exist_ok=True)
    
    try:

        image_processor = ImageProcessor(config, logger)
        browser_manager = BrowserManager(config, logger)
        

        resized_images = image_processor.resize_images()
        logger.info(f"Processed {len(resized_images)} images")
        
        # Initialize browser
        browser_manager.kill_chrome_processes()
        driver = browser_manager.initialize_driver()
 
        uploader = RestaurantUploader(driver, config, logger)
        
      
        df = pd.read_excel(config.EXCEL_FILE)
        logger.info(f"Loaded {len(df)} restaurants from Excel file")
        

        for index, row in df.iterrows():
            logger.info(f"Processing restaurant {index + 1}/{len(df)}: {row['name']}")
            uploader.upload_restaurant(row, resized_images)
            
    except Exception as e:
        logger.error(f"Fatal error: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()
            logger.info("Browser session closed")

if __name__ == "__main__":
    main()