import mailbox
import pandas as pd
import quopri
import re

def getDataFrame(mboxPath):
    box = mailbox.mbox(mboxPath)
    subjects = []
    expeditors = []
    contents = []

    for msg in box:
        subject = msg['Subject']
        expeditor = msg['From']
        content = extractContent(msg)
        cleanContent = deleteCodeText(content)
        subjects.append(subject)
        expeditors.append(expeditor)
        contents.append(cleanContent)

    data = {'from': expeditors, 'subject': subjects, 'content': contents}
    return pd.DataFrame(data)


def extractContent(msg):
    payload = msg.get_payload()
    if msg.is_multipart():
        for subMsg in payload:
            return extractContent(subMsg)
    else:
        if msg.get_content_type() == "text/plain":  # we get only plain/text message
            #try decoding from Content-Transfer-Encoding: quoted-printable
            try:
                return quopri.decodestring(payload).decode('utf-8')
            except ValueError:
                return payload
        else:
            return ""

def deleteCodeText(msg):
    msgWithoutBraces = re.sub(r'{((.|\n)(?!{))*}','',msg)
    msgWithoutParenthesis= re.sub(r'\(((.|\n)(?!\())*\)','',msgWithoutBraces)
    msgWithoutBracket = re.sub(r'\[((.|\n)(?!\[))*\]','',msgWithoutParenthesis)
    return msgWithoutBracket

