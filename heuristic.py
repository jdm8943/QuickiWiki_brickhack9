from io import StringIO
import re, string, pywikibot, lxml
from nltk import word_tokenize, WordNetLemmatizer, pos_tag
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
    

    # text preprocessing ideas from machinelearningknowledge.ai
    def remove_whitespace(text):
        return  " ".join(text.split())
    def remove_stopwords(text):
        en_stopwords = stopwords.words('english')
        # result = []
        # for token in text:
        #     if token not in en_stopwords:
        #         result.append(token)    
        # return result
        return " ".join([word for word in str(text).split() if word not in en_stopwords])
    # def remove_punct(text):
    #     tokenizer = RegexpTokenizer(r"\w+")
    #     lst=tokenizer.tokenize(' '.join(text))
    #     return lst
    def lemmatization(text):
        result=[]
        wordnet = WordNetLemmatizer()
        for token,tag in pos_tag(text):
            pos=tag[0].lower()
            if pos not in ['a', 'r', 'n', 'v']:
                pos='n'
            result.append(wordnet.lemmatize(token,pos))
        return result
    @staticmethod
    def preprocess(page) -> str:
        pagetext = page.get()
        doc = quw.nlp(pagetext)

        # dataframe = pd.read_csv(StringIO(pagetext), ["text"], on_bad_lines='skip').squeeze("columns")
        # dataframe = pd.read_html(page.full_url())
        # print(dataframe)
        # dfText = dataframe[['text']]
        # dfText['text'] = dfText['text'].str.lower()
        # dfText['text'] = dfText['text'].apply(
        #     Heuristics.remove_whitespace
        #     ).apply(
        #     lambda X: word_tokenize(X)
        #     ).apply(
        #     Heuristics.remove_stopwords
        #     ).apply(
        #     # remove_punct
        #     lambda x: re.sub('[%s]' % re.escape(string.punctuation), '' , x)
        #     ).apply(
        #     # remove numbers
        #     lambda x: re.sub('W*dw*','',x)
        #     ).apply(
        #     Heuristics.lemmatization
        #     )
        # return dfText['text']
    
    @staticmethod
    def compareDocBodies(currentPage):
        pass
        


if __name__=='__main__':
    quw = qw.Quikiwiki()
    curPage = pywikibot.Page(quw.site, "The Worlds of Doctor Who")
    print(Heuristics.checkCategoriesWithGoal(curPage))
    Heuristics.preprocess(quw.goalPage)