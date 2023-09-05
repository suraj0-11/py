marks = []
for i in range(3):
    mark = float(input(f"Enter mark for test {i+1}: "))
    marks.append(mark)

marks.sort(reverse=True)

best_average = (marks[0] + marks[1]) / 2

print(f"The best average mark out of the two highest scores is: {best_average:.2f}")
