import spacy
import heuristic, aStar, bfs
import pywikibot
import time

class Quikiwiki:

    def __init__(self):
        self.site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
        self.site.login()
        self.startPage = pywikibot.Page(self.site, "Doom (1993 video game)")
        self.goalPage = pywikibot.Page(self.site, "Dual Wield")
        #Wii Shop Channel
        #Yahoo! Games
        #Doom (1993 video game)
        #Devolver Digital
        
        # self.goalCategories = set(self.goalPage.categories())
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

    listStar = aStar.runAStar(qw.startPage, qw.goalPage, qw)
    listStar.reverse()
    print("A-Star Solution:")
    num = 0
    for i in listStar:
        print(num, "\t:", i)
        num+=1
    
    # listBFS = bfs.runBFS(qw.startPage, qw.goalPage, qw)
    # if(listBFS is False):
    #     print(":LAKSDJFF:LSDKAJD:SLFKJERFJKL:ERJOIP:FWEJOI:WERFT")
    # listBFS.reverse()
    # print("BFS Solution:")
    # num = 0
    # for i in listBFS:
    #     print(num, "\t:", i)
    #     num+=1

    endTime = time.time()
    print("TOTAL TIME: ", (endTime-startTime))

