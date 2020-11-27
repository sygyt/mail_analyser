
import MailParser as mp
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

import quopri
import re

def top_tfidf_feats(row, features, top_n=20):
    topn_ids = np.argsort(row)[::-1][:top_n]
    top_feats = [(features[i], row[i]) for i in topn_ids]
    df = pd.DataFrame(top_feats, columns=['features', 'score'])
    return df


def top_feats_in_doc(X, features, row_id, top_n=25):
    row = np.squeeze(X[row_id].toarray())
    return top_tfidf_feats(row, features, top_n)


df = mp.getDataFrame('data/input/personal_email/Personnel.mbox')
df_pro = mp.getDataFrame('data/input/work_email/Professionnelle.mbox')

#df = mp.fromEncodeUtf8ToDecode(df)
#df_pro = mp.fromEncodeUtf8ToDecode(df_pro)

#s = df.content[0]
#print(df.content[0])
#res = re.sub(r'{(.|\n)*}','',s)
#print(res)
#res2 = re.sub(r'\((.|\n)*\)','',res)
#print('RESSS 2 : ' + res2)

vect = TfidfVectorizer(stop_words='english', max_df=0.50, min_df=2)
X = vect.fit_transform(df.content)
Y = vect.fit_transform(df_pro.content)

features = vect.get_feature_names()
print(top_feats_in_doc(X, features, 1, 10))
print(top_feats_in_doc(Y, features, 1, 10))
