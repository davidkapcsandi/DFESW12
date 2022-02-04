def ICTGrade(h, a, f,):
    ICTPercentage = (h*a*f)*100
    return ICTPercentage
t= ICTGrade

students_name = input("What is your name?")
homework_score = int(input("Enter your score of your homework? "))/25
assessment_score = int(input ("Enter your score of you assessment? "))/50
final_exam_score = int(input ("Enter your score of final exam? "))/100
   

var1 = ICTGrade(homework_score, assessment_score, final_exam_score)
print(f"Your ICP percentage is: {var1}")

