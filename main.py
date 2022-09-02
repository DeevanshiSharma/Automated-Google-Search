from selenium import webdriver

def google_search():  
    # input from user
    st = input("Enter string/URL- ")
    # structuring the input for search
    search_string = st.replace(' ', '+') 
  
    # Assigning the browser variable with chromedriver of google chrome
    chrome_browser = webdriver.Chrome('chromedriver')
  
    # browsing the user input
    
    search_input = chrome_browser.get("https://www.google.com/search?q=" +
                                    search_string + "&start=" + 1)


if __name__ == "__main__":
    google_search()