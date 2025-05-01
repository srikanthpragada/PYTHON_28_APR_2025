# Show grade of an exam - A >= 80, B >= 60, C >= 50 or Failed

marks = int(input("Enter marks :"))

if marks >= 80:
    print('C')
elif marks >= 60:
    print('B')
elif marks >= 50:
    print('C')
else:
    print("Failed")


