"""
Patent Information Scraper

This script automates the extraction of patent summaries from OEPM and Patentscope websites.
It uses Selenium for browser automation and BeautifulSoup for HTML parsing,
storing the results in a MongoDB database.

Author: [Your Name]
Version: 1.0.0
Date: February 2025
"""

# Required library imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import tempfile
import time
from pymongo import MongoClient
import re

# MongoDB connection setup
# Establishes connection to local database "Proyecto" and collection "patentes"
client = MongoClient("mongodb://localhost:27017/")
db = client["Proyecto"]
collection = db["patentes"]

def get_dynamic_content_summary(university_url):
    """
    Extracts dynamic content summary from a specific URL.
    Uses Selenium for handling dynamic content and BeautifulSoup for HTML processing.
    
    Args:
        university_url (str): Target URL to process.

    Returns:
        str: Extracted summary text or None if not found.
    
    Raises:
        FileNotFoundError: If ChromeDriver is not found.
        Exception: For general execution errors.
    """
    driver = None
    temp_dir = None
    try:
        print(f"\nAttempting to access URL: {university_url}")
        
        # Create unique temporary directory for browser data
        temp_dir = tempfile.mkdtemp(prefix='chrome_', dir=os.path.expanduser('~'))

        # Configure Chrome browser options
        options = Options()
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        options.add_argument("--no-sandbox")  # Avoid sandboxing
        options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory usage
        options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
        options.add_argument("--window-size=1920,1080")  # Set window size
        options.add_argument(f"--user-data-dir={temp_dir}")  # Set user data directory
        options.add_argument("--disable-extensions")  # Disable browser extensions
        options.add_argument("--disable-notifications")  # Disable notifications
        options.binary_location = "/usr/bin/chromium-browser"  # Chromium browser path

        # Verify ChromeDriver executable existence
        CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"
        if not os.path.exists(CHROMEDRIVER_PATH):
            raise FileNotFoundError(f"ChromeDriver not found at path: {CHROMEDRIVER_PATH}")
        service = Service(CHROMEDRIVER_PATH)

        # Initialize Chrome browser
        driver = webdriver.Chrome(service=service, options=options)
        
        # Ensure URL has http/https prefix
        if not university_url.startswith(('http://', 'https://')):
            university_url = 'https://' + university_url
        
        # Pause to avoid overload before loading URL
        time.sleep(2)
        
        # Access URL and wait for body element
        driver.get(university_url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Process content based on detected domain
        if "consultas2.oepm.es" in university_url:
            print("OEPM domain detected")
            time.sleep(5)  # Additional wait for content loading
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')

            # Search for tables in the page
            tables = soup.find_all('table')
            print(f"Found {len(tables)} tables")
            for table in tables:
                # Look for cells containing "Resumen"
                summary_cell = table.find(string=lambda text: text and "Resumen" in text)
                if summary_cell:
                    # Extract summary text
                    summary_text = summary_cell.find_next('td')
                    if summary_text:
                        return summary_text.get_text(strip=True)
            print("Summary not found in OEPM tables")

        elif "patentscope" in university_url:
            print("Patentscope domain detected")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Resumen')]"))
            )
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Search for "Resumen" text
            summary_label = soup.find(string=lambda text: text and "Resumen" in text)
            if summary_label:
                summary_text = summary_label.find_next("span")
                if summary_text:
                    return summary_text.get_text(strip=True)
            print("Summary not found in Patentscope")
        else:
            print(f"URL not recognized as OEPM or Patentscope: {university_url}")

    except Exception as e:
        print(f"General error while obtaining summary: {e}")
        return None

    finally:
        # Ensure browser closure and temporary directory removal
        if driver:
            try:
                driver.quit()
            except:
                pass
        if temp_dir:
            try:
                import shutil
                shutil.rmtree(temp_dir)
            except:
                pass
    
    return None

# Initialize counters for process statistics
total_processed = 0
total_updated = 0

# Iterate through each document in MongoDB collection
for document in collection.find():
    total_processed += 1
    url = document.get("URL")
    if not url:
        print(f"Document {total_processed}: No URL, skipping.")
        continue

    # Clean URL by removing text between parentheses
    clean_url = re.sub(r'\s*\([^)]*\)', '', url).strip()
    print(f"\nDocument {total_processed}")
    print(f"Original URL: {url}")
    print(f"Clean URL: {clean_url}")

    # Get summary from URL
    summary = get_dynamic_content_summary(clean_url)

    if summary:
        print("Summary found, updating database...")
        collection.update_one({"_id": document["_id"]}, {"$set": {"summary": summary}})
        total_updated += 1
        print(f"Summary updated. Total updated: {total_updated}")
    else:
        print("Could not obtain summary for this URL.")

# Process summary
print(f"\nProcess completed:")
print(f"Total documents processed: {total_processed}")
print(f"Total documents updated: {total_updated}")
