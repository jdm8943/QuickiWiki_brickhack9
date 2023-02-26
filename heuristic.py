import math
import pywikibot
import quikiwiki as qw

class Heuristics:

    @staticmethod
    def calculateH(test):
        return 0

    @staticmethod
    # checks how many categories are the same between the current page and the goal
    def checkCategoriesWithGoal(currentPage):
        # print(str(category1.title()[9:]))
        # print(str(category2.title()[9:]))
        curCatSet = set(currentPage.categories())
        inverseJaccard = (1 - len(set.intersection(curCatSet, quw.goalCategories)) / len(set.union(curCatSet, quw.goalCategories))) * 100
        if inverseJaccard > 70:
            return inverseJaccard
        elif getHeurOfLink(currentPage)[0] < 50:
            return math.inf
        else:
            return inverseJaccard
        
    def getHeurOfLink(currentPage):
        pages = list(currentPage.linkedPages)
        arr = [len(pages)]
        return arr


if __name__=='__main__':
    quw = qw.Quikiwiki()
    curPage = pywikibot.Page(quw.site, "The Worlds of Doctor Who")
    print(Heuristics.checkCategoriesWithGoal(curPage))