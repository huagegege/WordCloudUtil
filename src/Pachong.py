
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="chromedriver", port=9515)
wait = WebDriverWait(driver, 10)

driver.get("https://music.163.com/")
driver.find_element_by_css_selector('#srch').send_keys('空心\n')
ifream = driver.switch_to.frame("contentFrame")

audio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#auto-id-NsA5W4Hg4N3RZuVS > div > div > div:nth-child(1) > div.td.w0 > div")))

url = audio.find_element_by_css_selector('a').get_attribute('href')

driver.get(url)