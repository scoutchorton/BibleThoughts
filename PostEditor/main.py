#Intro
print "BibleThoughts PostEditor"
version = 1.0
print "scoutchorton - 2017"
print "Type 'help' to read the help file to get commands if you get stuck."

#Imports
from os import system
from time import sleep

#Variables
global postsFile
global posts
global postID
global errorFile
global errorDict

#Referesh posts
def refPosts():
    postsFile = open('posts', 'w+')
    posts = eval(postsFile.read())
    postID = max(posts.keys())

#Startup
def boot():
    print "Starting PostEditor v. " + str(version)
    print "Initiating posts..."
    refPosts()
    print "Loading error dictonary..."
    errorFile = open('errors', 'r')
    errorDict = errorFile.read()

#Close
def exitFunction():
    print "Performing exit functions..."
    postsFile.close()
    errorFile.close()
    print "Exit functions complete.\nGoodbye!"
    exit()

#Prompt eroors
def

#Main prompt function
def prompt():
    p = raw_input("<: ").lower().split(" ")
    print p
    sleep(2)
    if p[0] == "help":
        system("cat helpFile | less")
    elif p[0] =="exit":
        exitFunction()
    elif p[0] == "posts":
         if len(p) == 0:
             print "Command 'posts'"
    else:
        print "Command not recognized. Retype the command, or enter 'help' to view commands."
    prompt()

#Run the program
prompt()
