# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# The next line imports the scraperwiki library
import scraperwiki
import lxml.html
#
print("Hello")
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
#This line shows the content of the website 
print(html)
#
record = {}
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print(root.cssselect("div#footer"))
print(root)
listofmatches = root.cssselect("a")
for match in listofmatches:
  print(match)
  print(lxml.html.tostring(match))
  record["link"] = lxml.html.tostring(match)
  print(record)
  scraperwiki.sqlite.save(unique_keys=["link"], data=record)
  
  
  
#
# # Write out to the sqlite database using scraperwiki library

#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
