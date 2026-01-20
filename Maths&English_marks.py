maths_score=int(input("What is your maths score?"))
english_score=int(input("What is your english score?"))
if maths_score>=90:
    if english_score>=90:
        print("You are good at everything")
    else:
        print("you are good at maths ")
else:
    print("You need to study maths properly")
if english_score>=90:
    print("You are good at English")
else:
    print("You need to study english properly")