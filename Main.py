import MailParser as mp
import Vectorizer as vctzr

df = mp.getDataFrame('data/input/personal_email/Personal.mbox')
df_pro = mp.getDataFrame('data/input/professional_email/Professional.mbox')

vect = vctzr.TfidfVectorizer(stop_words='english', max_df=0.50, min_df=2)
X = vect.fit_transform(df.content)
Y = vect.fit_transform(df_pro.content)

features = vect.get_feature_names()
# print the top 10 terms in document 1
print(vctzr.top_feats_in_doc(X, features, 1, 10))
print(vctzr.top_feats_in_doc(Y, features, 1, 10))

# print the top terms across all documents
print(vctzr.top_mean_feats(X, features, None, 0.1, 10))
print(vctzr.top_mean_feats(Y, features, None, 0.1, 10))
