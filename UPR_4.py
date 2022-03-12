import matplotlib.pyplot as plt
import pandas as pd

arr = pd.read_csv('StudentsPerformance.csv')
print(arr)

plt.figure()
plt.title('gender and race/ethnicity')
plt.scatter(x=arr['gender'],
            y=arr['race/ethnicity'])
plt.grid()

plt.figure()
plt.title('gender and parental level of education')
plt.scatter(x=arr['gender'],
            y=arr['parental level of education'])
plt.grid()

plt.figure()
plt.title('gender and lunch')
plt.scatter(x=arr['gender'],
            y=arr['lunch'])
plt.grid()

plt.figure()
plt.title('gender and parental level of education')
plt.scatter(x=arr['gender'],
            y=arr['parental level of education'])
plt.grid()

plt.figure()
plt.title('gender and test preparation course')
plt.scatter(x=arr['gender'],
            y=arr['test preparation course'])
plt.grid()

plt.figure()
plt.title('gender and math score')
plt.scatter(x=arr['gender'],
            y=arr['math score'])
plt.grid()

plt.figure()
plt.title('gender and reading score')
plt.scatter(x=arr['gender'],
            y=arr['reading score'])
plt.grid()

plt.figure()
plt.title('gender and writing score')
plt.scatter(x=arr['gender'],
            y=arr['writing score'])
plt.grid()

plt.figure()
plt.title('race/ethnicity and parental level of education')
plt.scatter(x=arr['race/ethnicity'],
            y=arr['parental level of education'])
plt.grid()

plt.figure()
plt.title('race/ethnicity and lunch')
plt.scatter(x=arr['race/ethnicity'],
            y=arr['lunch'])
plt.grid()

plt.figure()
plt.title('race/ethnicity and test preparation course')
plt.scatter(x=arr['race/ethnicity'],
            y=arr['test preparation course'])
plt.grid()

plt.figure()
plt.title('race/ethnicity and math score')
plt.scatter(x=arr['race/ethnicity'],
            y=arr['math score'])
plt.grid()

plt.figure()
plt.title('race/ethnicity and reading score')
plt.scatter(x=arr['race/ethnicity'],
            y=arr['reading score'])
plt.grid()

plt.figure()
plt.title('race/ethnicity and writing score')
plt.scatter(x=arr['race/ethnicity'],
            y=arr['writing score'])
plt.grid()

plt.figure()
plt.title('parental level of education and lunch')
plt.scatter(x=arr['parental level of education'],
            y=arr['lunch'])
plt.grid()

plt.figure()
plt.title('parental level of education and test preparation course')
plt.scatter(x=arr['parental level of education'],
            y=arr['test preparation course'])
plt.grid()

plt.figure()
plt.title('parental level of education and math score')
plt.scatter(x=arr['parental level of education'],
            y=arr['math score'])
plt.grid()

plt.figure()
plt.title('parental level of education and reading score')
plt.scatter(x=arr['parental level of education'],
            y=arr['reading score'])
plt.grid()

plt.figure()
plt.title('parental level of education and writing score')
plt.scatter(x=arr['parental level of education'],
            y=arr['writing score'])
plt.grid()

plt.figure()
plt.title('lunch and test preparation course')
plt.scatter(x=arr['lunch'],
            y=arr['test preparation course'])
plt.grid()

plt.figure()
plt.title('lunch and math score')
plt.scatter(x=arr['lunch'],
            y=arr['math score'])
plt.grid()

plt.figure()
plt.title('lunch and reading score')
plt.scatter(x=arr['lunch'],
            y=arr['reading score'])
plt.grid()

plt.figure()
plt.title('lunch and writing score')
plt.scatter(x=arr['lunch'],
            y=arr['writing score'])
plt.grid()

plt.figure()
plt.title('test preparation course and math score')
plt.scatter(x=arr['test preparation course'],
            y=arr['math score'])
plt.grid()

plt.figure()
plt.title('test preparation course and reading score')
plt.scatter(x=arr['test preparation course'],
            y=arr['reading score'])
plt.grid()

plt.figure()
plt.title('test preparation course and writing score')
plt.scatter(x=arr['test preparation course'],
            y=arr['writing score'])
plt.grid()

plt.figure()
plt.title('math score and reading score')
plt.scatter(x=arr['math score'],
            y=arr['reading score'])
plt.grid()

plt.figure()
plt.title('math score and writing score')
plt.scatter(x=arr['math score'],
            y=arr['writing score'])
plt.grid()

plt.figure()
plt.title('reading score and writing score')
plt.scatter(x=arr['reading score'],
            y=arr['writing score'])
plt.grid()

plt.show()
