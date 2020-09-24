"""

    1. Add the following line to your requirements.txt file:
       wikipedia==1.4.0

    2. Modify your Dockerfile to change the last line to this:
        CMD ["python3", "wikipedia-test.py"]

    3. Run the docker build command again:
        docker build . --tag project1:1.0

    4. Now run the docker run command to run this file:
        docker run --rm -it -v "$(pwd)/app:/app" project1:1.0

    Hopefully you can see how to integrate some of the code below into
    the main.py that you have been working on. If you have any
    questions, let me know.

    When you want to go back to working on main.py, change the last
    line of your Dockerfile back to what it was before:
        CMD ["python3", "wikipedia-test.py"]

    and then run the docker build command again, and docker run as you
    wish.

"""

import random

import wikipedia
import pronouncing

wikipedia_page = wikipedia.page("Kendrick_Lamar")

# This next line gets the textual content of the page and splits it up
# based on the characters ". " which creates a list of strings. The
# idea is that this would create a list of sentences, but it is not
# perfect
words_in_order = wikipedia_page.content.split(" ")

# Now you can proceed with the patterns from the tutorials, looking at
# any example where you have a list of strings. Some examples:


# Chooses a random sentence:
rhyming_word_list = []
while ( len(rhyming_word_list) < 10 ):
    random_number = random.randrange( len(words_in_order) )

    first_word = words_in_order[random_number]
    first_phrase = " ".join(words_in_order[random_number-5:random_number+1])

    print("sen: " + first_phrase)
    print("word: " + first_word + "\n")

    rhyming_word_list = pronouncing.rhymes(first_word)

print( str(rhyming_word_list) + "\n" )

second_word = ""
i = 0
second_word_list = []
while ( second_word not in rhyming_word_list and i < 1000 ):
    random_number = random.randrange( len(words_in_order) )

    second_word = words_in_order[random_number]
    second_phrase = " ".join(words_in_order[random_number-5:random_number+1])

    second_word_list.append(second_word)
    # print("sen 2: " + second_sentence)
    # print("word 2: " + second_sen_last_word + "\n")
    i = i + 1


if ( i == 1000 ):
    print("Fail. " + str(second_word_list[-20:]) )
else:
    print( "match (i = " + str(i) + ")" )

    print("\n\n" + first_phrase + "\n" + second_phrase + "\n")
    

    
