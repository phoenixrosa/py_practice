from bs4 import BeautifulSoup
import mechanize
import cookielib
import urllib

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar("cookies.txt")
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')]

# ================== #

URL = "https://dragcave.net/login"

br.open(URL)

br.form = list(br.forms())[0]
# these two come from the code you posted
# where you would normally put in your username and password
br["username"] = "chocopie"
br["password"] = "asdfdsa"
response = br.submit()
cj.save()

# ================== #

soup = BeautifulSoup(br.response().read(), "html5lib")

#print(soup.body)
logged_in_html = soup.find("div", class_="_3o_3")
print(logged_in_html)




