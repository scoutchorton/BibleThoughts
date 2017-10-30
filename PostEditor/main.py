#Version
version = 1.0

#Imports
from os import system
from time import sleep
import datetime

#Variables
postsPend = 0
filesToClose = []

#Referesh posts
def refPosts():
    global filesToClose
    global postsFileR
    global postID
    global posts
    if postsPend != 0:
        if raw_input("You have " + str(postsPend) + " post(s) pending. Press enter to override pending posts.") == "":
            postsFileR = open('posts', 'r+')
            if not (postsFileR in filesToClose): filesToClose.append(postsFileR)
            posts = eval(postsFileR.read())
            postID = max(posts.keys())
    else:
        postsFileR = open('posts', 'r+')
        if not (postsFileR in filesToClose): filesToClose.append(postsFileR)
        posts = eval(postsFileR.read())
        postID = max(posts.keys())

#New posts
def newPost():
    global tempFile
    global postsPend
    name = raw_input("  -Post Title-<: ")
    postDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
    tempFile = open('tempFile', 'w+')
    raw_input("You are about to edit the message of the post. Press enter to continue: ")
    system("nano tempFile")
    messa = tempFile.read()[:-1]
    print "Title: " + name + "\nDate: " + postDate + "\nMessage:\n" + messa
    approve = raw_input("  Press enter to accept:")
    if approve != "":
        newPost()
    else:
        posts[postID+1] = [name, postDate, messa]
        postsPend += 1

#Apply posts
def postsApply():
    global postsFileW
    global postsPend
    postsFileW = open('posts', 'w')
    postsFileW.write(str(posts))
    print "Posts saved to file."
    postsFileW.close()
    postsPend = 0
    refPosts()

#Close
def exitFunction():
    print "Performing exit functions..."
    for i in filesToClose:
        i.close()
    print "Exit functions complete.\nGoodbye!"
    exit()

#Prompt errors
def throwError(erID):
    print "Err" + str(erID) + " " + errorDict[erID][0] + ": " + errorDict[erID][1]

#Main prompt function
def prompt():
    if postsPend != 0:
        print "You have " + str(postsPend) + " post(s) pending."
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
            refPosts()
        elif p[1] == "new":
            newPost()
        elif p[1] == "apply":
            if postsPend == 0:
                print "You have no posts pending."
            else:
                postsApply()
        elif p[1] == "list":
            tempFile = open('tempFile', 'w').close()
            tempFile = open('tempFile', 'a')
            for i in posts.keys():
                tempFile.write("Name: " + posts[i][0] + "\nID: " + str(i) + "\nDate: " + posts[i][1] + "\nMessage: " + posts[i][2] + "\n\n")
            tempFile.close()
            system("cat tempFile | less")
        else:
            throwError(103)
    else:
        throwError(101)
    prompt()

#Startup
def boot():
    global filesToClose
    global errorFile
    global errorDict
    print "Booting..."
    print "Initiating posts..."
    refPosts()
    print "Loading error dictonary..."
    errorFile = open('errors', 'r')
    filesToClose.append(errorFile)
    errorDict = eval(errorFile.read())
    print "Finished init. Starting PostEditor v. " + str(version) + "..."
    print "\n\n\nBibleThoughts PostEditor"
    print "scoutchorton - 2017"
    print "Type 'help' to read the help file to get commands if you get stuck."
    prompt()

#Start
boot()
