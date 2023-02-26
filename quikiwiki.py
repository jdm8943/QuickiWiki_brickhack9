import heuristic, aStar, spacy
import pandas as pd
import pywikibot
import time

class Quikiwiki:

    def __init__(self):
        self.site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
        self.site.login()
        self.startPage = pywikibot.Page(self.site, "Doom (1993 video game)")
        # self.goalPage = pywikibot.Page(self.site, "Doom_(2016_video_game)")
        self.goalPage = pywikibot.Page(self.site, "Yahoo! Games")
        self.goalCategories = set(self.goalPage.categories())
        self.nlp = spacy.load("en_core_web_md")
        # self.goalLinks = self.nlp(heuristic.Heuristics.preprocessLinks(self.goalPage, self))
        self.goalTitle = self.nlp(heuristic.Heuristics.preprocessTitle(self.goalPage, self))

    
    # def processGoalText():
    #     self.

if __name__=='__main__':
    startTime = time.time()
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
    endTime = time.time()
    print("TOTAL TIME: ", (endTime-startTime))

