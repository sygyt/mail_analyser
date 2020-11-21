import mailbox
import csv

def showMbox(mboxPath):
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        box = mailbox.mbox(mboxPath)
        for msg in box:
            msg_playload = extractContent(msg)
            print (msg_playload)
            spamwriter.writerow([msg['From'],msg['To'],msg['Subject'],msg_playload])
            #showPayload(msg) 


def extractContent(msg):
    payload = msg.get_payload()
    if msg.is_multipart():
        for subMsg in payload:
            return extractContent(subMsg)
    else:
        if (msg.get_content_type() == "text/plain"):
            return payload
        else :
            return "we not kept not plain/text message"
 

def showPayload(msg):
    payload = msg.get_payload()

    if msg.is_multipart():
        div = ''
        for subMsg in payload:
            print (div)
            showPayload(subMsg)
            div = '------------------------------'
    else:
        if (msg.get_content_type() == "text/plain"):
            print ("main type : " + msg.get_content_maintype())
            print (msg.get_content_type())
            print (payload)
            payload
        else :
            print("we not print not plain/text message")


if __name__ == '__main__':
    showMbox('data/input/personal_email/Personnel.mbox')