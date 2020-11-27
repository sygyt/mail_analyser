import mailbox
import pandas as pd
import quopri

def getDataFrame(mboxPath):
    box = mailbox.mbox(mboxPath)
    subjects = []
    expeditors = []
    contents = []

    for msg in box:
        subject = msg['Subject']
        expeditor = msg['From']
        content = extractContent(msg)
        if content is None: # The variable
            print('It is None')
        subjects.append(subject)
        expeditors.append(expeditor)
        contents.append(content)

    data = {'from': expeditors, 'subject': subjects, 'content': contents}
    return pd.DataFrame(data)


def extractContent(msg):
    payload = msg.get_payload() ##change here
    if msg.is_multipart():
        for subMsg in payload:
            return extractContent(subMsg)
    else:
        if msg.get_content_type() == "text/plain":  # we get only plain/text message
            #try decoding from Content-Transfer-Encoding: quoted-printable
            try:
                return quopri.decodestring(payload)
            except ValueError:
                print("ERROR : " + payload)
                return payload
        else:
            return ""


#def test(x):
#    return quopri.decodestring(x).decode('utf-8') if x != "" else x
     
#def fromEncodeUtf8ToDecode(df):
#    return df.applymap(lambda x: test(x))