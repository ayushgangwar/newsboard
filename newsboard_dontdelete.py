from selenium import webdriver
from selenium.webdriver.common.keys import Keys
URL="https://www.google.com/search?q="
driver = webdriver.Chrome()
keywords=['reliance','tatasteel']

for i in  keywords:
    url_new=URL+str(i)
    driver.get(url_new)
    driver.find_element_by_xpath("//*[contains(text(), 'News')]").click()
    for j in range(1,3):
        title=driver.find_element_by_xpath("//*[@id='rso']/div["+str(j)+"]/g-card/div/div/a/div/div[2]/div[2]").text
        url=driver.find_element_by_xpath("//*[@id='rso']/div["+str(j)+"]/g-card/div/div/a/div/div[2]/div[2]").text
        src=driver.find_element_by_xpath("//*[@id='rso']/div["+str(j)+"]/g-card/div/div/a/div/div[2]/div[1]/span").text
        description=driver.find_element_by_xpath("//*[@id='rso']/div["+str(j)+"]/g-card/div/div/a/div/div[2]/div[3]").text
        print("title, url, src, description",title, url, src, description)