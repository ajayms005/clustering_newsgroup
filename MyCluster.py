#created by Ajay M S

from MyTokenizer import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn import feature_extraction
import pandas as pd
import mpld3


def cluster(docDump,docContentList,noOfClusters):
    print "start clustering"
    totalvocab_stemmed = []
    totalvocab_tokenized = []

    for doc in docContentList:
        allwords_stemmed = tokenize_and_stem(doc)
        totalvocab_stemmed.extend(allwords_stemmed)
        
        allwords_tokenized = tokenize_only(doc)
        totalvocab_tokenized.extend(allwords_tokenized)
    
    
    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    

    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000, min_df=0.2, stop_words='english', use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))
    tfidf_matrix = tfidf_vectorizer.fit_transform(docContentList)
    terms = tfidf_vectorizer.get_feature_names()
    dist = 1 - cosine_similarity(tfidf_matrix)
    
    km = KMeans(n_clusters=noOfClusters)
    km.fit(tfidf_matrix)
    clusters = km.labels_.tolist()

    joblib.dump(km,  'doc_cluster.pkl')
    km = joblib.load('doc_cluster.pkl')
    clusters = km.labels_.tolist()
    clusterDict={}
    for i in range(0,noOfClusters):
        clusterDict[i]=[]
    for i in range(0,len(clusters)):
        clusterNo=clusters[i]
        clusterDict[clusterNo].append(docDump[i])
    return clusterDict
