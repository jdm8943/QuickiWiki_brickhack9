import pywikibot

class Heuristics:

    @staticmethod
    def calculateH():
        pass

    @staticmethod
    def checkSameCategory(category1, category2):
        # print(str(category1) + str(category2))
        pass


if __name__=='__main__':
    site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
    site.login()
    page = pywikibot.Page(site, "The Worlds of Doctor Who")
    categories = page.categories()
    Heuristics.checkSameCategory(next(categories), next(categories))