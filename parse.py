from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def parse_new(last_movie):  # last_movie is a last movie we parsed last time
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    elem_titles = []
    movies = []
    page = 1
    while last_movie not in elem_titles:
        driver.get("http://moviestape.net/katalog_filmiv/page/"+str(page)+"/")

        # here we get all the information about movies on the page
        elem_titles = driver.find_elements_by_class_name('title')
        elem_years = driver.find_elements_by_class_name('ycc')
        elem_urls = driver.find_elements_by_xpath(
            "//div[@class='conteiner']/div[@class='left']/div[@id='dle-content']/div[@class='bnewmovie']/a")
        elem_imgs = driver.find_elements_by_xpath(
            "//div[@class='conteiner']/div[@class='left']/div[@id='dle-content']/div[@class='bnewmovie']/a/img")

        elem_titles = [elem_titles[elem].text for elem in range(len(elem_titles))]  # creating list of title strings
        # and here we combine it into one list of dictionaries
        for elem in range(len(elem_titles)):
            if elem_titles[elem] == last_movie:  # stop executing loop on last_movie
                break
            movie = {
                "title": elem_titles[elem],
                "year": elem_years[elem].text,
                "href": elem_urls[elem].get_attribute("href"),
                "img": elem_imgs[elem].get_attribute("src")
            }
            movies.append(movie)

        if last_movie == '':  # If file last_movie.txt is empty we parse only first page
            break
        page += 1

    driver.close()
    return movies
