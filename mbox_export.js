cursor = db.getCollection('mailing-lists').find();
print('subject\tmessage');
while (cursor.hasNext()) {
    jsonObject = cursor.next();
    print("\"" + jsonObject.subject + "\"\t\"" + jsonObject.thread.join(' ').replace(/[\""]/g, '\\"')  + "\"");
}