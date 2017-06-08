# dbpedia-dialogue-data
    
    Not using virtualenv right now probably will in the future
    http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
    virtualenv dbpedia-dialogue-data
    virtualenv -p /usr/local/bin/python3.6 dbpedia-dialogue-data # Or wherever you have python3 installed

    source dbpedia-dialogue-data/bin/activate
    mongoimport -d dbpedia --drop -c mailing-lists --jsonArray < dbpedia-discussion-archive-questions.json
    mongoexport -d dbpedia -c mailing-lists -q '{$query: {thread_length: {$gte: 10}}, $orderby: {thread_length: -1} } ' -o out.json