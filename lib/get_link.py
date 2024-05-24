from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

# Replace with your webdriver path
driver = webdriver.Chrome()  

# Target the subreddit URL
url = "https://www.reddit.com/r/stories"
driver.get(url)

time.sleep(10)
actions = ActionChains(driver)
actions.scroll_by_amount(0, 500).perform()

html_content = driver.page_source

driver.quit()

soup = BeautifulSoup(html_content, "html.parser")

all_posts = soup.find_all(name='a')

# Extract text from each post
all_links = []
old_link = ''
for post in all_posts:
    link = post["href"]
    if '/r/stories/comments' in link and link != old_link and 'https' not in link:
      all_links.append(link)
      old_link = link

# Print all extracted link
index = 0
for link in all_links:
  print(f"index {index} : ",link)
  index +=1
with open ('Links.txt','w') as wr :
  wr.writelines("\n".join(all_links))