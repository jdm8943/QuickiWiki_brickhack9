from io import StringIO
import re, string, pywikibot, lxml
from nltk.corpus import stopwords
import pandas as pd
import quikiwiki as qw

class Heuristics:


    @staticmethod
    def calculateH(page):
        Heuristics.checkCategoriesWithGoal(page)

    @staticmethod
    # checks how many categories are the same between the current page and the goal
    def checkCategoriesWithGoal(currentPage):
        # print(str(category1.title()[9:]))
        # print(str(category2.title()[9:]))
        curCatSet = set(currentPage.categories())
        inverseJaccard = 1 - len(set.intersection(curCatSet, quw.goalCategories)) / len(set.union(curCatSet, quw.goalCategories))
        return inverseJaccard
    

    @staticmethod
    def preprocess(page, quw) -> str:
        pagetext = page.get()
        doc = quw.nlp(pagetext.lower())
        result = {}
        for token in doc:
            if token.text in quw.nlp.Defaults.stop_words:
                continue
            if token.is_punct:
                continue
            if token.lemma_ == '-PRON-':
                continue
            newtokens = re.split("[][{}\|/=.]", token.lemma_)
            for t in newtokens:
                if t not in result:
                    result[t] = 1
                else:
                    result[t] += 1
        print(result)
        return " ".join(result.keys())
    
    @staticmethod
    def compareBodyText(currentPage, quw):
        curText = quw.nlp(Heuristics.preprocess(currentPage, quw))
        return curText.similarity(quw.goalText)
        


if __name__=='__main__':
    quw = qw.Quikiwiki()
    STOP_WORDS = quw.nlp.Defaults.stop_words
    # print(STOP_WORDS)
    curPage = pywikibot.Page(quw.site, "The Worlds of Doctor Who")
    # print(Heuristics.checkCategoriesWithGoal(curPage))
    sim = Heuristics.compareBodyText(curPage, quw)
    print(curPage.title() + " vs " + quw.goalPage.title() + ": " + str(sim))