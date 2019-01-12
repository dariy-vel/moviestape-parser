from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from mail import send_mail

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("http://moviestape.net/katalog_filmiv/")
elem_titles = driver.find_elements_by_class_name('title')
elem_years = driver.find_elements_by_class_name('ycc')
elem_urls = driver.find_elements_by_xpath(
    "//div[@class='conteiner']/div[@class='left']/div[@id='dle-content']/div[@class='bnewmovie']/a")
elem_imgs = driver.find_elements_by_xpath(
    "//div[@class='conteiner']/div[@class='left']/div[@id='dle-content']/div[@class='bnewmovie']/a/img")
movies = []
for elem in range(len(elem_titles)):
    movie = {
        "title": elem_titles[elem].text,
        "year": elem_years[elem].text,
        "href": elem_urls[elem].get_attribute("href"),
        "img": elem_imgs[elem].get_attribute("src")
    }
    movies.append(movie)

send_mail(movies)
driver.close()
