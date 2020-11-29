import MailParser as mp
import Vectorizer as vctzr

import quopri
import re

df = mp.getDataFrame('data/input/personal_email/Personal.mbox')
df_pro = mp.getDataFrame('data/input/professional_email/Professional.mbox')

#df = mp.fromEncodeUtf8ToDecode(df)
#df_pro = mp.fromEncodeUtf8ToDecode(df_pro)

#s = df.content[0]
#print(df.content[0])
#res = re.sub(r'{(.|\n)*}','',s)
#print(res)
#res2 = re.sub(r'\((.|\n)*\)','',res)
#print('RESSS 2 : ' + res2)

vect = vctzr.TfidfVectorizer(stop_words='english', max_df=0.50, min_df=2)
X = vect.fit_transform(df.content)
Y = vect.fit_transform(df_pro.content)

features = vect.get_feature_names()
print(vctzr.top_feats_in_doc(X, features, 1, 10))
print(vctzr.top_feats_in_doc(Y, features, 1, 10))