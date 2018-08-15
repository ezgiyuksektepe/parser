from HTMLParser import HTMLParser
import urllib2

f = open('ezgi.csv','wb')

class Ezgi(HTMLParser):

    save = False

    f.write("URL, Job Title, Location")

    def handle_starttag(self, tag, attr):
        i = 0

        if tag == "a" and ("rel", "nofollow") in attr and ("class", "h2") in attr:
            self.save = True

            for name, value in attr:
                if name == "href":
                        f.write("\n" + "https://www.besmith.com" + value + ",")

        if tag == "h4":
        	self.save = True

    def handle_endtag(self, tag):
        if tag == "h4":
            self.save = False
        if tag == "a":
            self.save = False

    def handle_data(self, data):
        if self.save:
            clean = data.strip() + ","
            f.write(clean)

fullPage = urllib2.urlopen("https://www.besmith.com/candidates/search-listings/?page=2")
byteArray = fullPage.read()
decoded = byteArray.decode("utf-8")
decoded = decoded.replace(",", "")

parser = Ezgi()
parser.feed(decoded)
f.close()