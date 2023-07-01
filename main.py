import random

hello_replies = ["Hello", "Hey there", "How you doing?", "What's up", "Hi there"]

while True:
    query = input("Say something : ")
    if query != "exit":
        if query == "hello" or query == "hi":
            print(random.choice(hello_replies))
    elif query == "exit":
        print("Bye.")
        break