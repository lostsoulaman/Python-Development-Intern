# import library
import time

String = "Hello this is Aman kumar"

wordcount = len(String.split())
print(String)

while True:
    t0=time.time()

    # taking input from user
    inputtext=str(input("Enter the sentence:- "))
    t1=time.time()
    accuracy=len(set(inputtext.split()) & set(String.split()))

    # calculating accuracy
    accuracy=accuracy/wordcount

    # calculating time taken
    timetaken=t1-t0

    # calculating words per minute
    wpm=wordcount/timetaken

    # printing all these three values
    print("Words Per Minute:- ",wpm,"\nAccuracy:- ",accuracy,"\nTime Taken:- ",timetaken)
