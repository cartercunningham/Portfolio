from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

def mars_news(browser):
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    browser.visit(url)
    html = browser.html
    article_soup = BeautifulSoup(html, "html.parser")

    title_results = article_soup.find('div', class_='content_title')
    title_results

    teaser_results = article_soup.find('div', class_='article_teaser_body')
    teaser_results

    # return news_title, news_p
    for result in title_results:
        news_title = title_results.find('a').text

    for result in teaser_results:
        news_p = teaser_results.text

    return news_title, news_p


def featured_image(browser):
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # Retrieve page with the requests module
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(3)
    browser.click_link_by_partial_text('more info')
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")
    image=(image_soup.find('figure',class_="lede")).find('a')['href']

    # Use the base url to create an absolute url
    img_url = "https://www.jpl.nasa.gov"+image
    return img_url


def hemispheres(browser):
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Retrieve page with the requests module
    browser.visit(url)

    # Retrieve Cerberus
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    html = browser.html
    cerberus_soup = BeautifulSoup(html, "html.parser")
    cerberus_image="https://astrogeology.usgs.gov"+(cerberus_soup.find('div',class_="wide-image-wrapper")).find('img',class_="wide-image")['src']
    print(cerberus_image)

    # Retrieve Schiaparelli
    browser.visit(url)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    html = browser.html
    schiaparelli_soup = BeautifulSoup(html, "html.parser")
    schiaparelli_image="https://astrogeology.usgs.gov"+(schiaparelli_soup.find('div',class_="wide-image-wrapper")).find('img',class_="wide-image")['src']
    print(schiaparelli_image)

    # Retrieve Syrtis
    browser.visit(url)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    html = browser.html
    syrtis_soup = BeautifulSoup(html, "html.parser")
    syrtis_image="https://astrogeology.usgs.gov"+(syrtis_soup.find('div',class_="wide-image-wrapper")).find('img',class_="wide-image")['src']
    print(syrtis_image)

    # Retrieve Valles
    browser.visit(url)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    html = browser.html
    valles_soup = BeautifulSoup(html, "html.parser")
    valles_image="https://astrogeology.usgs.gov"+(valles_soup.find('div',class_="wide-image-wrapper")).find('img',class_="wide-image")['src']
    print(valles_image)

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_image},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_image},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_image},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_image},
    ]

    return hemisphere_image_urls

def twitter_weather(browser):
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    browser.visit(url)
    html = browser.html
    tweet_soup = BeautifulSoup(html, "html.parser")

    #this returns the most recent tweet, including retweets - couldn't get it to return only the most recent weather tweet
    tweet_results = tweet_soup.find('div', class_='js-tweet-text-container')
    # tweet_results1 = tweet_soup.find('div', data-screen-name_='MarsWXReport') - this was one of the attempts at pulling Mars Weather only

    # return news_title, news_p
    for tweet in tweet_results:
        mars_weather = tweet_results.find('p').text

    return mars_weather

def mars_facts():
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    url = 'http://space-facts.com/mars/'

    # Retrieve page with the requests module
    browser.visit(url)

    # Scrape table using Pandas, save as df
    table = pd.read_html(url)
    mars_facts=pd.DataFrame(table[0])

    # return df as html
    mars_facts_html= mars_facts.to_html(header = False, index = False)
    mars_facts_html

    return mars_facts_html

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
