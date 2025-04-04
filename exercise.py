file1 = []
with open("file1.txt", "r") as file1_data:
    file1 = [int(line.strip()) for line in file1_data]

file2 = []
with open("file2.txt", "r") as file2_data:
    file2 = [int(line.strip()) for line in file2_data]
    

result = [number for number in file1 if number in file2]  

print(result)

# print(file1)
# print(file2)