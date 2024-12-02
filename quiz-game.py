print("Welcome to my quiz")

playing =  input("Do you want to play? ").lower()

if playing != "yes":
  quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What does CLI stand for? ").lower()
if answer == "command line interface":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does API stand for? ").lower()
if answer == "application programming interface":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does SDK stand for? ").lower()
if answer == "software development kit":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does HTTPS stand for? ").lower()
if answer == "hypertext transfer protocol secure":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does JSON stand for? ").lower()
if answer == "javascript object notation":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")
  
answer = input("What does CRUD stand for? ").lower()
if answer == "create, read, update, delete":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does ORM stand for? ").lower()
if answer == "object relational mapping":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does SQL stand for? ").lower()
if answer == "structure query language":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does Saas stand for? ").lower()
if answer == "software as a service":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does DevOps stand for? ").lower()
if answer == "development and operations":
    print("Correct!")
    score += 1
else: 
  print("Incorrect!")

answer = input("What does DNS stand for? ").lower()
if answer == "domain name system":
    print("Correct!")
    score += 1
else:
  print("Incorrect!")

print("You got " + str(score) + " out of 11 questions correct!")
percentage = (score / 11) * 100
print("Which is equivalent to " + str(round(percentage)) + "%.")
