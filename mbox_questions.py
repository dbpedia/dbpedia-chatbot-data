# encoding: utf-8

import csv
import json
import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")

question_words = ['what', 'when', 'why', 'which', 'who', 'how', 'whose', 'whom']

csv_reader = csv.reader(open('data/dbpedia-discussion-archive.csv', 'r'))

def is_question_topic(subject, message):
    global question_words, question_topics, questions
    if subject in question_topics or any(s in subject.lower() for s in question_words) or any(s in message.lower() for s in question_words):
        if subject not in questions.keys():
            questions[subject] = {
                "thread": []
            }
        questions[subject]['thread'].append(u'' + message)
        return True
    else:
        return False

question_topics = set()
questions = {}

count = 0
for line in csv_reader:
    if is_question_topic(line[3], line[4]):
        question_topics.add(line[3])
        print line[3]
        count += 1

print count
print len(questions.keys())

with open('data/dbpedia-discussion-archive-questions.json', 'w') as fp:
    json.dump(questions, fp)