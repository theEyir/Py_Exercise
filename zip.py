print("----------------------- zip() -----------------------")

data_1 = [2, 4, 5, 8, 5, 1, 13]
data_2 = [5, 7, 8, 9, 6, 0]

print(zip(data_1, data_2))
print(list(zip(data_1, data_2)))
print(dict(zip(data_1, data_2)))

myTuple = [(3, 4), (9, 0), (39, 42), (12, 453), (56, 84), (4, 6), (0, 1)]

print(zip(*myTuple))
print(list(zip(*myTuple)))

students = ['amin', 'ahmad', 'omid', 'sina', 'ali']
mid_terms = [87, 90, 94, 83, 99.5]
last_grade = [94, 94, 95, 93, 98]

final_grade = {nums[0] : (nums[1] + nums[2])/2 for nums in zip(students, mid_terms, last_grade)}
print("\nThis year grades is : ", final_grade)
