#Example where the text file contents are read in and sent as the search parameter to the specified url

import urllib
import os

def read_text():
        current_dir = os.getcwd()
        # os.getcd() is used to allow the sample file to be run regardless of the location if this folder is copied as is
        quotes = open(current_dir + "/movie_quotes.txt")
        contents_of_file = quotes.read()
        print(contents_of_file)
        quotes.close()
        check_profanity(contents_of_file)

def check_profanity(text_to_check):
        connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
        output = connection.read()
        connection.close()
        if "true" in output:
                print("Profanity Alert!")
        elif "false" in output:
                print("This document contains no curse words!")
        else:
                print("Could not scan the selected document.")

read_text()
