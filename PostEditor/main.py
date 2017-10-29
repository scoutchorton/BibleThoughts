#Version
version = 1.0

#Imports
from os import system
from time import sleep

#Variables
postsFile = None
posts = None
postID = None
errorFile = None
errorDict = None

#Referesh posts
def refPosts():
    postsFile = open('posts', 'w+')
    posts = eval(postsFile.read())
    postID = max(posts.keys())

#Close
def exitFunction():
    print "Performing exit functions..."
    postsFile.close()
    errorFile.close()
    print "Exit functions complete.\nGoodbye!"
    exit()

#Prompt eroors
def throwError(erID):
    print "Err" + str(erID) + " " + errorDict[erID][0] + ": " + errorDict[erID][1]

#Main prompt function
def prompt():
    p = raw_input("<: ").lower().split(" ")
    if p[0] == "help":
        system("cat helpFile | less")
    elif p[0] =="exit":
        exitFunction()
    elif p[0] == "posts":
        if len(p) == 1:
            throwError(102)
        elif p[1] == "refresh":
            print "Refreshing list of posts..."
        elif p[1] == "new":
            pass #Work on this...
        else:
            throwError(103)
    else:
        throwError(101)
    prompt()

#Startup
def boot():
    global errorDict
    print "Booting..."
    print "Initiating posts..."
    #refPosts()
    print "Loading error dictonary..."
    errorFile = open('errors', 'r')
    errorDict = eval(errorFile.read())
    print "Finished init. Starting PostEditor v. " + str(version) + "..."
    print "\n\n\nBibleThoughts PostEditor"
    print "scoutchorton - 2017"
    print "Type 'help' to read the help file to get commands if you get stuck."
    prompt()

#Start
boot()
