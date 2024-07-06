# 1) Write a program that takes a student's score as input and prints their Marksheet on predefined grading criteria.

a=int(input("enter your marks!"))
if(a>=90 and a<=100):
    {
        print("Your grade is A+")
    };
elif(a>=80):{
    print("Your grade is A ")
};
elif(a>=70):{
    print("YOUr grade is B")
};
elif(a>=60):{
    print("Your grade is C")
};
else:{
    print("You  are fail!")
}