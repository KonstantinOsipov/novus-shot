from selenium import webdriver
import time
import random
from fake_useragent import UserAgent


url = "https://nftsport.novus.team/"

user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]

useragent = UserAgent()

#options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Chrome(
    executable_path="D:\Work\novus-shot\chromedriver",
    options=options
)

try:
    driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    time.sleep(5)

except Exception as ex:
        print(ex)
finally:
    driver.close()
    driver.quit()
