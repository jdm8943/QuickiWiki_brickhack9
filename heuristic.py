import pywikibot
import

class Heuristics:

    @staticmethod
    def calculateH(page):
        pass

    @staticmethod
    # checks how many categories are the same
    def checkCategoriesWithGoal():
        # print(str(category1.title()[9:]))
        # print(str(category2.title()[9:]))
        cat1 = str(category1.title()[9:])   # strings containing names of two categories
        cat2 = str(category2.title()[9:])
        pass


if __name__=='__main__':
    site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
    site.login()
    page = pywikibot.Page(site, "The Worlds of Doctor Who")
    categories = page.categories()
    Heuristics.checkSameCategory(next(categories), next(categories))