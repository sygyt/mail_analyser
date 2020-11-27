"""Print out text of emails from MBox file."""

from collections import Counter
import mailbox
import sys
import re




def remove_r(text):
  return text.replace("\r", "")


def strip_replies(text):
  lines = text.split("\n")
  lines = [l for l in lines if len(l) > 0]
  lines = [line for line in lines if line[0] != ">"]
  return "\n".join(lines)


def strip_footer(text):
  text, _ = re.subn("On (Sun|Mon|Tue|Wed|Thu|Fri|Sat),.*, 20.. at.*@gmail.com.*wrote.*",
                    "",
                    text,
                    flags=re.DOTALL)
  text, _ = re.subn("You received this message because you are subscribed to the Google Groups.*",
                    "",
                    text,
                    flags=re.DOTALL)
  return text


def get_core_text(msg):
  msg = get_text(msg)
  msg = remove_r(msg)
  msg = strip_replies(msg)
  #msg = strip_footer(msg)
  return msg



def get_text(msg):
  while msg.is_multipart():
    msg = msg.get_payload()[0]
  return msg.get_payload()


def print_msgs(msg_list, f=sys.stdout):
  for msg in msg_list:
    print("-------------------------------------------------------------------", file=f)
    #print("Subject:", msg["subject"], file=f)
    print("", file=f)
    print(get_core_text(msg), file=f)
    print("", file=f)



mbox = mailbox.mbox("data/input/personal_email/Personnel.mbox")


c = Counter(m["from"] for m in mbox)
#print(c.most_common(10))

for message in mbox.itervalues():
    print("Subject:", message["subject"])
    print(get_core_text(message))

#print_msgs(msgs)