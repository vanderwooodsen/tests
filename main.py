
import first_test
import second_test
import third_test
print()
print("Hello! Welcome to the tests!") 
print()
print("We have three tests for you, please choose test which you want:\n",
  "1) Test with fact from fiction; \n" ,
  "2) Phython test;\n", 
  "3) Personality test.")
print()
choose_test = input("> ")
print("You choose test : ",choose_test)
print()
print("You can exit from the test whatever you want, just type 'exit'. ")
print()
print("Lets go")
print()



def run_test(test):
  
  total_score = 0

  for question in test["questions"]:
    print(question["Question"], "\n")

    answers = question["answers"]
    answers_list = list(answers.keys())
    #print(answers_list)

    for i in range(len(answers_list)):
      print("{}. {}".format(i+1, answers_list[i]))

    print()

    while True:
      guest_answer = input("Please choose  your answer - ")

      if guest_answer == "exit":
        print("Thanks for your visit 😊")
        return

      if not guest_answer.isdigit():
        print("Please select a number from answers!")
        continue

      guest_answer = int(guest_answer) -1

      if guest_answer >= len(answers_list):
        print("Please select a number from answers!")
        print()
        continue
      break
    selected_answer = answers_list[guest_answer]
    print()
    print("Your answer is: ", selected_answer)
    print()

    question_score = answers[selected_answer]
    total_score += question_score



  print("Your total score is: {}".format(total_score))
  if total_score >= test["min_score"]:
    print(test["score_more_message"])
    picture_file = test["score_more_picture"]
    print(open(picture_file, "r").read())

  else:
    print(test["score_less_message"])
    picture_file = test["score_less_picture"]
    print(open(picture_file, "r").read())




if choose_test == "1":
  print(" If you think you know fact from fiction, try to answer these true and false questions correctly!\n", 
  " At this test you can get 25 points. ") 
  print(" Please choose True or False ")
  print(" Good luck!😋 ")
  print()
  run_test(first_test.test())

elif choose_test == "2":
  print(" We  have a few questions to determine your python knowledge!😊\n", 
  " Maximum score is 45 points.\n", 
  " Good Luck!😋")
  print()
  run_test(second_test.test())

elif choose_test == "3":
  print(" This is a personality test, it will help you understand whether introvert or extravert you are. Begin each statement with “I….” ")
  print()
  run_testД(third_test.test())