import operator 
import itertools

def makesubsearches(new_q): # insert a list of queries
    phrases = []
    for i in range(len(new_q)):
        subphrases = list(itertools.combinations(new_q, i+1))
        phrases.extend(subphrases)
    searches = []
    for search in phrases: 
        string = ""
        for i in range(len(search)):
            string += " " + search[i] 
        searches.append(string)
    searches.sort(cmp=bylength)
    searches.reverse()
    return searches
    # [' free ', ' wifi ', ' coffee ', ' free wifi', 
    # ' free coffee', ' wifi coffee ', ' free wifi coffee']

def bylength(word1, word2):
    return len(word1) - len(word2)

def transformreview(review):
    # strip out punctuation or plural form
    # eg, "dish." => "dish"; "pizzas" => pizza
    doc = review.lower()
    transform = []
    for word in doc.split():
        if word[-1] in ",.!s":
            word = word[:-1]
        transform.append(word)
    transformed = " ".join(transform)
    return transformed

def makerank(new_q, review):
    doc = transformreview(review)
    location_dict = {} # dict of {location: length}
    i = 0
    irange = len(doc.split()) 
    searches = makesubsearches(new_q)
    while i < irange:   
        for search in searches:
            s_length = len(search.split()) # check how long the 
            # search term is  
            if search in doc:
                doc_list = doc.split()
                search_list = search.split()
                location = doc_list.index(search_list[0])
                location_dict[location] = s_length
                i = i + s_length
            else:
                i = i + 1
    rank = sorted(location_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    result = (rank, location_dict)
    return result # return a tuple, 
    # r, sorted one for finddensity, location_dict, 
    # dictioanry to access length of matched keywords

    # pair[1] is the starting location of the matched string
    # eg, (1,205) ie, doc[205]+doc[206]+doc[207] = deep dish pizza

def finddensity(r, total_length):
    # compare rank 1 with any other ones 
    # return the closest other keyword, ranked by the best match
    # ie, "deep dish pizza" and another "deep dish pizza" 
    # will rank higher than two "pizza"s

    distance_pair = [] # list of dictionary with value of 
        # tuples [rank: [(distance, (location1, location2),(distance, 
        # (location1, location2)], rank: ] 
        # [ distance, (location1, location2) ]
    for i in range(len(r)):
        if r[i][1] == 3:
            for j in range(i+1, len(r)):
                distance = abs(r[i][0] - r[j][0])
                max_distance = total_length - r[i][1] - r[j][1]
                pair = ((r[i][1] + r[j][1], distance),(r[i][0], r[j][0]))
                if distance <= max_distance:
                    distance_pair.append(pair)

        if r[i][1] == 2:
            for j in range(i+1, len(r)):
                distance = abs(r[i][0] - r[j][0])
                max_distance = total_length - r[i][1] - r[j][1]
                pair = ((r[i][1] + r[j][1], distance), (r[i][0], r[j][0]))
                if distance <= max_distance:
                    distance_pair.append(pair)

        if r[i][1] == 1:
            for j in range(i+1, len(r)):
                distance = abs(r[i][0] - r[j][0])
                max_distance = total_length - r[i][1] - r[j][1]
                pair = ((r[i][1] + r[j][1], distance), (r[i][0], r[j][0]))
                if distance <= max_distance:
                    distance_pair.append(pair)

    pair = sorted(distance_pair)
    pair.reverse()
    # [((4, 18), (134, 152)), ((3, 31), (152, 121)), 
    # ((3, 31), (134, 165)), ((3, 24), (134, 110)), ((3, 21), 
    # (264, 243)), ((3, 13), (152, 165)), ((3, 13), (134, 121)), 
    # ((2, 11), (110, 121))]
    return pair[0] # so the most matches, & 
    # closest one comes first 

def makesentence(pair, length_dict, doc, total=40):
    start_point = min(pair[1][0], pair[1][1])
    end_point = max(pair[1][0], pair[1][1])
    # print "make1" , start_point, end_point # ok 
    word_list = makefirst(start_point, end_point, doc, length_dict)
    # print "word_list", word_list
    sentence_start = findsentencebeginning(start_point, doc)
    long_word_list = makefullsentence(sentence_start, doc, word_list, start_point, total)
    sentence = " ".join(long_word_list)
    return sentence 

def makefirst(start_point, end_point, doc, length_dict): 
    word_list = []
    j = length_dict[end_point]
    for i in range(start_point, end_point+j):
        word = doc[i]
        word_list.append(word)
    return word_list

def findsentencebeginning(start_point, doc):
    sentence_start = 0
    if start_point == 0:
        sentence_start = start_point
    else:
        for i in range(start_point, 0, -1): 
        # start checking indices 
        # before the startpoint 
            if doc[i][-1] in ".!?":
                sentence_start = i + 1
                break
            else:
                continue
    return sentence_start

def makefullsentence(sentence_start, doc, word_list, start_point, total_length):
    new_word_list = []
    # end_point = sentence_start + total_length + 1
    i = sentence_start
    while i < start_point: # 117 to 148       
        new_word_list.append(doc[i])
        i += 1
    new_word_list.extend(word_list)
    while len(new_word_list) < total_length:
        new_word_list.append(doc[i])
        i += 1
    return new_word_list

def addhighlight(sentence, query):
    final_list = []
    query = query.split()
    for word in sentence.split():
        if word.lower() in query:
            word = "[[HIGHLIGHT]]" + word + "[[ENDHIGHLIGHT]]"
        final_list.append(word)
    for i in range(len(final_list)-1):
        if final_list[i][-16:] == final_list[i+1][-16:]:
            final_list[i] = final_list[i][:-16]
            # '[[Highlight]]dish'
            final_list[i+1] = final_list[i+1][13:]
            # 'dish[[ENDhighlight]]'
    final_sentence = " ".join(final_list)
    return final_sentence

def main():
    review = open('text.txt','r')
    raw_doc = review.readlines() # returns a list 
    doc_string = "".join(raw_doc)
    doc = doc_string.split() # make a list of words
    print "What would you like to search for?"
    print " (eg, 'deep dish pizza', or 'pizza friend')"
    query = raw_input("> ")
    new_q = " ".join(query.split()).lower() 
    # remove extra space and make them all lower case
    result = makerank(new_q.split(), doc_string)
    if len(result[0]) <= 1:
        # stop the algorithm if only 1 word is found
        stop_statement = "Search not found, try another term?"
        print stop_statement
        return stop_statement # stop the search

    pair = finddensity(result[0], 40)
    sentence = makesentence(pair, result[1], doc)
    final_sentence = addhighlight(sentence, query)
    print "Here is your relevant snippet:"
    print final_sentence

if __name__ == '__main__':
    main()

