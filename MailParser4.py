import mailbox
import pandas as pd

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
    
    data = {'from':expeditors,'subject':subjects,'content':contents}
    df = pd.DataFrame(data)
    return df

def extractContent(msg):
    payload = msg.get_payload()
    if msg.is_multipart():
        for subMsg in payload:
            return extractContent(subMsg)
    else:
        if (msg.get_content_type() == "text/plain"): #we get only plain/text message
            return payload
        else :
            return ""


df = getDataFrame('data/input/personal_email/Personnel.mbox')
print(df)