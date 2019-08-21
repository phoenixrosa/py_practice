#from bs4 import BeautifulSoup

from selenium import webdriver

chrome_driver_path = "/Users/christopherryu/Projects/py_practice/wp/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
br = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)

# ================== #

URL = "https://wolfplaygame.com/index.php"

br.get(URL)

##br.form = list(br.input())[0]
# these two come from the code you posted
# where you would normally put in your username and password
##print(br.form.controls)
#br["sname"] = "venus"
#br["pwd"] = "verbatim1"
#response = br.submit()
#cj.save()

# ================== #

#soup = BeautifulSoup(br.response().read(), "html5lib")

#print(soup.body)
#logged_in_html = soup.find("div", class_="_3o_3")
#print(logged_in_html)




