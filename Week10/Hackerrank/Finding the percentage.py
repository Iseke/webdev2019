n = int(input())
student_marks = []
for _ in range(n):
    student_marks.append([e for e in input().split()])
nme = input()
res = [float(m)+float(p)+float(c) for name, m, p, c in student_marks if name == nme]
print("{0:.2f}".format(res[0] / 3))