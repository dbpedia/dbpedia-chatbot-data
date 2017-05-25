import csv
import mailbox
import re

def clean_content(content, subject=False):
    if subject:
        content = re.sub(r'\[.*\]\s?', '', content) # Remove reply and name of mailing list from subject
        content = re.sub(r'Re\s?:\s?', '', content, flags=re.I)
        content = re.sub(r'Fwd\s?:\s?', '', content, flags=re.I)
    else:
        sign_index = content.find('--')
        if sign_index != -1:
            content = content[:sign_index]

    content = re.sub(r'<.*?>', '', content, flags=re.MULTILINE) # Remove HTML Tags
    content = content.replace('&nbsp;', '').replace('&quot;', '') # Removing Whitespace characters need to be extended to others as required

    # content = re.sub(r'http\S+', '', content, flags=re.MULTILINE) # Removing HTTP Links. Need to decide if this is needed
    content = re.sub(r'^>.*(\n|$)', ' ', content, flags=re.MULTILINE) # Remove Reply Sections

    #content = content.replace('&gt;', '').replace('&lt;', '').replace('&eq;', '')  # Comparison Characters
    content = content.strip().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ') # Removes newlines, tabs etc.
    content = re.sub(r'\s{2,}', ' ', content, flags=re.MULTILINE) # Remove extra whitespaces
    return content

def get_message_body(message):
    message_body = ""
    if message.is_multipart():
        for part in message.get_payload():
            message_body += get_message_body(part)
    else:
        message_body = message.get_payload(decode=True)
    return clean_content(message_body)

mbox = mailbox.mbox('data/dbpedia-discussion-archive')
csv_writer = csv.writer(open('data/dbpedia-discussion-archive.csv', 'wb'))
file_writer = open('data/dbpedia-discussion-archive-subjects.txt', 'w')

subjects = set()

for message in mbox:
    subject = clean_content(message['Subject'], True)
    csv_writer.writerow([message['Date'], message['Message-ID'], message['From'], subject, get_message_body(message)])
    subjects.add(subject)

for subject in subjects:
    file_writer.write("%s\n" % subject)