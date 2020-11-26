import mailbox
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


def getDataFrame(mboxPath):
    box = mailbox.mbox(mboxPath)
    subjects = []
    expeditors = []
    contents = []

    for msg in box:
        subject = msg['Subject']
        expeditor = msg['From']
        content = extractContent(msg)
        subjects.append(subject)
        expeditors.append(expeditor)
        contents.append(content)

    data = {'from': expeditors, 'subject': subjects, 'content': contents}
    return pd.DataFrame(data)


def extractContent(msg):
    payload = msg.get_payload()
    if msg.is_multipart():
        for subMsg in payload:
            return extractContent(subMsg)
    else:
        if msg.get_content_type() == "text/plain":  # we get only plain/text message
            return payload
        else:
            return ""


def parse_raw_message(raw_message):
    lines = raw_message.split('\n')
    email = {}
    message = ''
    keys_to_extract = ['from', 'to']
    for line in lines:
        if ':' not in line:
            message += line.strip()
            email['body'] = message
        else:
            pairs = line.split(':')
            key = pairs[0].lower()
            val = pairs[1].strip()
            if key in keys_to_extract:
                email[key] = val
    return email


def parse_into_emails(messages):
    emails = [parse_raw_message(message) for message in messages]
    return {
        'body': map_to_list(emails, 'body'),
        'to': map_to_list(emails, 'to'),
        'from_': map_to_list(emails, 'from')
    }


def map_to_list(emails, key):
    results = []
    for email in emails:
        if key not in email:
            results.append('')
        else:
            results.append(email[key])
    return results


def top_tfidf_feats(row, features, top_n=20):
    topn_ids = np.argsort(row)[::-1][:top_n]
    top_feats = [(features[i], row[i]) for i in topn_ids]
    df = pd.DataFrame(top_feats, columns=['features', 'score'])
    return df


def top_feats_in_doc(X, features, row_id, top_n=25):
    row = np.squeeze(X[row_id].toarray())
    return top_tfidf_feats(row, features, top_n)


df = getDataFrame('data/input/personal_email/Personnel.mbox')
df_pro = getDataFrame('data/input/work_email/Professionnelle.mbox')

vect = TfidfVectorizer(stop_words='english', max_df=0.50, min_df=2)
X = vect.fit_transform(df.content)
Y = vect.fit_transform(df_pro.content)

features = vect.get_feature_names()
print(top_feats_in_doc(X, features, 1, 10))
print(top_feats_in_doc(Y, features, 1, 10))

#print(df)
