from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def get_comments(video_url, count = 100):
    driver = webdriver.Chrome()
    driver.get(video_url)

    comments = []
    while len(comments) < count:
        scroll_pause_time = 2
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            WebDriverWait(driver, scroll_pause_time).until(
                lambda driver: driver.execute_script("return document.documentElement.scrollHeight") > last_height
            )
            last_height = driver.execute_script("return document.documentElement.scrollHeight")
            if last_height >= 5000:
                break

        comment_elements = driver.find_elements(By.CSS_SELECTOR, "#content-text")

        comments = [comment.text for comment in comment_elements]

    driver.quit()
    return comments[:count]