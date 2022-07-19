# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 09:48:03 2022
@author: HP NOTE
"""

'''
Q1 다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
'''
# shirt 가 문장안에 없으므로 shirt 를 출력한다.

'''
Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
'''
Sum = []
N = 1
while N <= 1000:
    if N % 3 == 0:
        Sum.append(N)
    N += 1
print(sum(Sum))

'''
Q3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
*
**
***
****
*****
'''
a = 0
while a < 5:
    a += 1
    print('*' * a) # 문자열 곱하기
    
'''
Q4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
'''
num = []
for i in range(1,101):
    num.append(i)
    if len(num) == 100:
        break
print(num)

'''
Q5 A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for문을 사용하여 A 학급의 평균 점수를 구해 보자.
'''
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
Sum = 0
for i in range(len(A)):
    Sum += A[i]
Avg = Sum / len(A)
print(Avg)

'''
Q6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
'''
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)