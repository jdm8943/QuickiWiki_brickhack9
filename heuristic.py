import math
import pywikibot
import quikiwiki as qw

class Heuristics:

    @staticmethod
    def calculateH(page, qw):
        return 0
        # return Heuristics.checkCategoriesWithGoal(page, qw)

    @staticmethod
    # checks how many categories are the same between the current page and the goal
    def checkCategoriesWithGoal(currentPage, quw):
        # print(str(category1.title()[9:]))
        # print(str(category2.title()[9:]))
        curCatSet = set(currentPage.categories())
        inverseJaccard = (1- len(set.intersection(curCatSet, quw.goalCategories)) / len(set.union(curCatSet, quw.goalCategories))) * 100
        return inverseJaccard
        # if inverseJaccard > 70:
        #     return inverseJaccard
        # elif Heuristics.getHeurOfLink(currentPage)[0] < 100:
        #     return math.inf
        # else:
        #     print("asdf", inverseJaccard)
        #     return inverseJaccard
        
    def getHeurOfLink(currentPage):
        pages = list(currentPage.linkedPages)
        arr = [len(pages)]
        return arr


if __name__=='__main__':
    quw = qw.Quikiwiki()
    curPage = pywikibot.Page(quw.site, "The Worlds of Doctor Who")
    print(Heuristics.checkCategoriesWithGoal(curPage))