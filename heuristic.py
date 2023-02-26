import math
import re, pywikibot
import quikiwiki as qw
import time

class Heuristics:


    @staticmethod
    def calculateH(page, qw):
        # return Heuristics.checkCategoriesWithGoal(page, qw)
        return 1 - Heuristics.compareTitle(page, qw)

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
            for token in newtokens:
                t = re.sub(r"[\n\t\s]*", "", token)
                if t not in result:
                    result[t] = 1
                else:
                    result[t] += 1
        # print(result)
        return " ".join(result.keys())
    
    @staticmethod
    def preprocessLinks(page, quw):
        linktext = " ".join(page.title() for page in page.linkedPages())
        doc = quw.nlp(linktext.lower())
        result = []
        for token in doc:
            if token.text in quw.nlp.Defaults.stop_words:
                continue
            if token.is_punct:
                continue
            if token.lemma_ == '-PRON-':
                continue
            # newtokens = re.split("[][{}\|/=.]", token.lemma_)
            # for token in newtokens:
            #     t = re.sub(r"[\n\t\s]*", "", token)
            result.append(token.lemma_)
        # print(result)
        return " ".join(result)
    
    @staticmethod
    def preprocessTitle(page, quw):
        doc = quw.nlp(page.title().lower())
        result = []
        for token in doc:
            if token.text in quw.nlp.Defaults.stop_words:
                continue
            if token.is_punct:
                continue
            if token.lemma_ == '-PRON-':
                continue
            # newtokens = re.split("[][{}\|/=.]", token.lemma_)
            # for token in newtokens:
            #     t = re.sub(r"[\n\t\s]*", "", token)
            result.append(token.lemma_)
        # print(result)
        return " ".join(result)
    
    @staticmethod
    def compareBodyText(currentPage, quw):
        curText = quw.nlp(Heuristics.preprocess(currentPage, quw))
        return curText.similarity(quw.goalText)
    
    @staticmethod
    def compareLinks(currentPage, quw):
        curLinks = quw.nlp(Heuristics.preprocessLinks(currentPage, quw))
        return curLinks.similarity(quw.goalLinks)
    
    @staticmethod
    def compareTitle(currentPage, quw):
        curTitle = quw.nlp(Heuristics.preprocessTitle(currentPage, quw))
        return curTitle.similarity(quw.goalTitle)


if __name__=='__main__':
    quw = qw.Quikiwiki()
    # print(STOP_WORDS)
    curPage = pywikibot.Page(quw.site, "Doom (1993 video game)")
    # print(Heuristics.checkCategoriesWithGoal(curPage))
    # textsim = Heuristics.compareBodyText(curPage, quw)
    # linksim = Heuristics.compareURLS(curPage, quw)
    # print(curPage.title() + " vs " + quw.goalPage.title() + ": " + str(textsim))
    # print([urlparse(canonicalize_url(link)).query for link in list(curPage.interwiki())])
    start = time.time()
    print(Heuristics.compareTitle(curPage, quw))
    print("took: " + str(time.time()-start))