import heuristic, aStar
import pywikibot

class Quikiwiki:

    def __init__(self):
        self.site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
        self.site.login()
        self.goalPage = pywikibot.Page(self.site, "The Worlds of Doctor Who")

if __name__=='__main__':
    qw = Quikiwiki()
    print("RAHHH! quikiwiki running!")
    print(qw.site)
    print(qw.goalPage.title())

