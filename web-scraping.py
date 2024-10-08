#Import urlopen() to be used to open urls within the program
from urllib.request import urlopen
import re #import regex

def retrieve_html_contents(input_url):
    local_url = input_url

    page = urlopen(local_url)

    local_html_bytes = page.read() #Extracts HTML from the webpage
    local_html = local_html_bytes.decode("utf-8") #Decodes HTML into a string using UTF-8
    return local_html

url = "http://olympus.realpython.org/profiles/aphrodite"
html = retrieve_html_contents(url)

print(html) # Prints the HTML contents

title_index = html.find("<title>") #Finds the index of the first occurence of the substring. In this case "<title>"
print(title_index)

#To get the index of the title itself (not the title tag), you can enter the following
start_index = title_index + len("<title>")
print(start_index)

#To find the end of the title in the HTML
end_index = html.find("</title>")
print(end_index)

#Now that we have the indexes of the start and end of the title, we can splice the html to get the title
title = html[start_index:end_index]
print(title)

#Trying a new HTML page
url = "http://olympus.realpython.org/profiles/poseidon"
html = retrieve_html_contents(url)

print(html) # Prints the HTML contents


url = "http://olympus.realpython.org/profiles/dionysus"
html = retrieve_html_contents(url)

pattern = "<title.*?>.*?</title.*?>" #Pattern to search for title
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group() # returns first and most inclusive result
title = re.sub("<.*?>", "", title) #Remove HTML tags
print(title)

