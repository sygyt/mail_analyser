#%pylab inline
import mailbox
import pandas as pd
import bs4

def get_html_text(html):
    try:
        return bs4.BeautifulSoup(html, 'lxml').body.get_text(' ', strip=True)
    except AttributeError: # message contents empty
        return None

def _get_email_messages(email_payload):
    for msg in email_payload:
        if isinstance(msg, (list,tuple)):
            for submsg in _get_email_messages(msg):
                yield submsg
        elif msg.is_multipart():
            for submsg in _get_email_messages(msg.get_payload()):
                yield submsg
        else:
            yield msg

def _read_email_text(email_data):
    email_payload = email_data.get_payload()
    if email_data.is_multipart():
        print('multipart')
        email_messages = list(_get_email_messages(email_payload))
        return email_messages
    else:
        email_messages = [email_payload]
        message_content_list = []
        for msg in email_messages:
            content_type = 'NA' if isinstance(msg, str) else msg.get_content_type()
            encoding = 'NA' if isinstance(msg, str) else msg.get('Content-Transfer-Encoding', 'NA')
            if 'text/plain' in content_type and 'base64' not in encoding:
                msg_text = msg.get_payload()
            elif 'text/html' in content_type and 'base64' not in encoding:
                msg_text = get_html_text(msg.get_payload())
            elif content_type == 'NA':
                msg_text = get_html_text(msg)
            else:
                msg_text = None
            message_content_list.append((content_type, encoding, msg_text))
            #print(msg_text)
        return message_content_list



mb = mailbox.mbox('data/input/personal_email/Personnel.mbox')

keys = ['Date', 'Subject','X-Gmail-Labels']
message_list = []

 
    dmessage = dict(message.items())
    #_read_email_text(message)
    print(_read_email_text(message))
    message_list.append({key:dmessage[key] if key in dmessage.keys() else '' for key in keys})

#print len(message_list), 'messages'
#print '**'*50
print(len(message_list))
message_list[:3]


 