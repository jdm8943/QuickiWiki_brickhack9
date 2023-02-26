import heuristic, aStar, spacy
import pandas as pd
import pywikibot

class Quikiwiki:

    def __init__(self):
        self.site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
        self.site.login()
        self.startPage = pywikibot.Page(self.site, "Doom (1993 video game)")
        # self.goalPage = pywikibot.Page(self.site, "Doom_(2016_video_game)")
        self.goalPage = pywikibot.Page(self.site, "Yahoo! Games")
        self.goalCategories = set(self.goalPage.categories())
        self.nlp = spacy.load("en_core_web_sm")
    
    # def processGoalText():
    #     self.

if __name__=='__main__':
    qw = Quikiwiki()
    print("RAHHH! quikiwiki running!")
    print(qw.site)

    # print(qw.goalPage.title())
    # listStar = aStar.runAStar(qw.startPage, qw.goalPage)
    # listStar.reverse()
    # print("ASTAR::::::::")
    # num = 0
    # for i in listStar:
    #     print(num, ":", i)
    #     num+=1

