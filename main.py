import random

hello_replies = ["Hello", "Hey there", "How you doing?", "What's up", "Hi there"]

while True:
    query = input("Say something : ")
    if query != "exit":
        if "hi" in query.lower() or "hello" in query.lower():
            print(random.choice(hello_replies))
        elif query.lower() == "roll a dice":
            print("You got",random.randint(0,6),".")
    elif query == "exit":
        print("Bye.")
        break
    else:
        print("Sorry, couldn't understand that.")
