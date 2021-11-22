from selenium import webdriver


def google_search():  
    # input from user
    search_string = input("What is the string or URL you want to search ?  ")
  
    # structuring the input for search
    search_string = search_string.replace(' ', '+') 
  
    # Assigning the browser variable with chromedriver of google chrome
    chrome_browser = webdriver.Chrome('chromedriver')
  
    # browsing the user input
    for i in range(1):
        search_input = chrome_browser.get("https://www.google.com/search?q=" +
                                        search_string + "&start=" + str(i))


# calling the google_search function
while True:
    google_search()