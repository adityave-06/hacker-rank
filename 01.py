n = int(input("Enter number of scores : "))
print("Enter the scores : ") 
arr = []
for i in range(n):
    scores = float(input())
    arr.append(scores)
arr = sorted(set(arr))
print(arr)
print(f"Highest score : {arr[-1]}")
print(f"Runner-Up score : {arr[-2]}")