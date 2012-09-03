A) Pizzeria.py is the main algorithm
Roadmap: 
1. Work on the query. 
- makesubsearches(new_q): Given a few keywords, create a list of possible combinations
- transformreview(review): Strip out punctuations / variations of words in reviews, so that "dish." == "dish" and "pizzas" == "pizzas"
- makerank(new_q, review): Make a rank based on query and the review, so that we know where the best match is located in the review

2. Construct result sentence
- makesentence: main function that has a list of subfunction that handles different parts of the sentence creation process
- makefirst: make a list of words that contains two closest matches (eg, "pizza" and "deep dish")
- findsentencebeginning: find the beginning of the sentence by searching the closest "." or "!" or "?"
- makefullsentence: make full sentence by limiting the word count to 40. 

3. Add highlight to the keywords
- Search again for the snippet and insert [[Highlight]] and [[Endhighlight]]


B) Pizzatest.py is the Unit Test I ran

C) Used Pylint to improve formatting. Score 8.90 (see pylint_pizzeria.txt)
Common issues raised include line too long, missing docstring, variable name too short
- Kept "r" as a single letter variable to conserve line length of finddensity function

D) Possible improvements
1. Work on expanding the transformreview function.
- Currently it only takes in punctuation. I'd add plural (dish == dishes), stop words (ignore search terms like "are/is/the" etc) and tenses (lower priority as I assume search terms are more likely to be nouns)

2. Allow for only 1 found item
- Currently the search only works if it finds more than 1 results
- That's due to my attempt to constructing a sentence of two closest keywords 

3. Expand on the Unit tests
