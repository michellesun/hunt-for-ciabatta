import unittest
import pizzeria

class PizzaTest(unittest.TestCase):
    ''' Main class for testing; Can be added to a suite'''
    # The function "setUp" will always be ran in order to setup the
    # test environment before all the tests have run.
    def setUp(self):
        '''Verify environment is setup properly''' # Print if test fails
        pass

    # The function "tearDown" will always be ran in order to cleanup the
    # test environment after all the tests have run.
    def tearDown(self):
        '''Verify environment is tore down properly''' # Print if test fails
        pass

    def test_finddensity(self):
        # function: finddensity(r,total_length)
        # return the most matches, & closest one comes first, 
        self.assertEqual(pizzeria.finddensity([(41, 1), (10, 1), (3, 1)],40), ((2, 38), (41, 3)) ) # Test will fail if "false" (boolean)


    def test_sentencebeginning(self):
        # function: findsentencebeginning(start_point,doc)
        # return sentence_Start
        self.assertEqual(pizzeria.findsentencebeginning(10,['whoa', 'whoa', 'a', 'coffee', 'shop', 'that', 'opens', 'past', '8pm?', 'their', 'coffee', 'is', 'even', 'good', "(i'm", 'drinking', 'it', 'right', 'now.)', 'ok', "i'm", 'gonna', 'station', 'myself', 'here', 'for', 'the', 'rest', 'of', 'the', 'summer.', 'Street', 'parking', 'isnt', 'bad.', 'Found', 'my', 'favorite', 'study', 'spot', 'in', 'SF.', 'Free', 'wifi,', 'great', 'chill', 'atmosphere,', 'not', 'too', 'busy', 'with', 'people', 'coming', 'in', 'and', 'going', 'out', 'when', "I'm", 'trying', 'to', 'get', 'some', 'work', 'done,', 'great', 'variety', 'of', 'medium', 'tempo', 'music', 'that', 'doesnt', 'make', 'me', 'sleepy', 'or', 'too', 'amped,', 'and', "I'm", 'actually', 'motivated', 'by', 'all', 'the', 'other', 'people', 'here', 'getting', 'their', 'work', 'done.', 'Win!']),9)

    def test_makefullsentence(self):
      # function : makefullsentence(sentence_start,start_point,word_list,doc,total_length) 
      # return long_word_list
      # makefullsentence(sentence_start, doc, word_list, start_point, total_length):
      self.assertEqual(pizzeria.makefullsentence(9,"whoa whoa a coffee shop that opens past 8pm? their coffee is even good (i'm drinking it right now.) ok i'm gonna station myself here for the rest of the summer.  Street parking isnt bad. Found my favorite study spot in SF. Free wifi, great chill atmosphere, not too busy with people coming in and going out when I'm trying to get some work done, great variety of medium tempo music that doesnt make me sleepy or too amped, and I'm actually motivated by all the other people here getting their work done. Win!".split(),['coffee', 'is', 'even', 'good', "(i'm", 'drinking', 'it', 'right', 'now.)', 'ok', "i'm", 'gonna', 'station', 'myself', 'here', 'for', 'the', 'rest', 'of', 'the', 'summer.', 'Street', 'parking', 'isnt', 'bad.', 'Found', 'my', 'favorite', 'study', 'spot', 'in', 'SF.', 'Free'],10,40),['their', 'coffee', 'is', 'even', 'good', "(i'm", 'drinking', 'it', 'right', 'now.)', 'ok', "i'm", 'gonna', 'station', 'myself', 'here', 'for', 'the', 'rest', 'of', 'the', 'summer.', 'Street', 'parking', 'isnt', 'bad.', 'Found', 'my', 'favorite', 'study', 'spot', 'in', 'SF.', 'Free', 'coffee', 'is', 'even', 'good', "(i'm", 'drinking'])

def main():
    ## overall data input
    # review = "whoa whoa a coffee shop that opens past 8pm? their coffee is even good (i'm drinking it right now.) ok i'm gonna station myself here for the rest of the summer.  Street parking isnt bad. Found my favorite study spot in SF. Free wifi, great chill atmosphere, not too busy with people coming in and going out when I'm trying to get some work done, great variety of medium tempo music that doesnt make me sleepy or too amped, and I'm actually motivated by all the other people here getting their work done. Win!"
    # doc = review.split()
    # q = "Free Wifi Coffee"
    # new_q = " ".join(q.split()).lower() 
    # word_list = ['free', 'wifi,', 'great', 'chill', 'atmosphere,', 'not', 'too', 'busy', 'with', 'people', 'coming', 'in', 'coffee']
    # long_word_list = ['Found', 'my', 'favorite', 'study', 'spot', 'in', 'SF','free', 'wifi,', 'great', 'chill', 'atmosphere,', 'not', 'too', 'busy', 'with', 'people', 'coming', 'in', 'and', 'going', 'out', 'when', "I'm", 'trying', 'to', 'get', 'some', 'work', 'done,']
    unittest.main()

if __name__ == '__main__':
    main()