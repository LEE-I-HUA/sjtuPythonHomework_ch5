def main():
    print("change the student's grade to score")
    score = eval (input("student's score:"))

    if (score <= 100 & score >= 90):
        grade = "A"
    elif(score <=89  & score >= 80):
        grade = "B"
    elif(score <=79  & score >= 70):
        grade = "C"
    elif(score <=69  & score >= 60):
        grade = "D"
    else:
        grade = "F"
    print("the student's grade is", grade)
main()
input()
