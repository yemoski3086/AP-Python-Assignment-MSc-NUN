# 1a Store your name in a variable, and print a message about the python class Your message should be simple, such as, “Hello {Your Name}, I am taking some Python classes?” Additionally, print your name in lowercase, uppercase, and titlecase and repeat sentences respectively
student_name = "Najeeb"
Najeeb = "Hello, i am taking some Python classes"
print(student_name)
print(student_name +" "+ Najeeb.lower()) #print LowerCase
print(student_name +" "+ Najeeb.upper()) #Print UpperCase
print(student_name +" "+ Najeeb.title())\


# b Find a quote from a famous person you admire and store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message with the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
famous_person = 'Malcoom X'
Message = "\"ounce said, A man who stands for nothing will fall for anything\"."
print(famous_person +  Message) #concartination.


# c Store the names of a few of your classmates in a list called names. Print each person’s name by accessing each element in the list, one at a time. Also, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
Classmates = ["sadeeq", "kemy", "jabir","abdulhamid"]
print(Classmates[0])
print(Classmates[1])
print(Classmates[2])
print(Classmates[3])
for x in Classmates:
    print("Hello, " + x + " I would like to invite you to my birthday party")
