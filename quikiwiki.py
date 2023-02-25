import heuristic, aStar
import pywikibot

class Quikiwiki:

    def __init__(self):
        self.site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
        self.site.login()
        self.startPage = pywikibot.Page(self.site, "Doom (1993 video game)")
        # self.goalPage = pywikibot.Page(self.site, "Doom_(2016_video_game)")
        self.goalPage = pywikibot.Page(self.site, "Wii Shop Channel")
        
        self.goalCategories = set(self.goalPage.categories())

if __name__=='__main__':
    qw = Quikiwiki()
    print("START:", qw.startPage.title())
    print("GOAL:", qw.goalPage.title())
    listStar = aStar.runAStar(qw.startPage, qw.goalPage)
    listStar.reverse()
    print("A-Star Solution:")
    num = 0
    for i in listStar:
        print(num, "\t:", i)
        num+=1

