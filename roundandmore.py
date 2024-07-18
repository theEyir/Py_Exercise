print("----------------------- len() -----------------------")
data = 'Inja Iran Ast'
print(len(data))
print(data.__len__())

print("\n----------------------- abs() -----------------------\n")

print(f"+ + 5 = {abs(5)} , - - 5 = {abs(-5)}")

print("\n----------------------- sum() -----------------------\n")

nums = [5, 3, 2, 10]
print(sum(nums))
print(sum(nums, 10))

print("\n----------------------- round() -----------------------\n")

print(round(4.75))
print(round(4.23))
print(round(4.1354733851, 4))