
high_scores = [78, 56, 67]
print("High scores:")
for i, score in enumerate(high_scores, start=1):
    print(f"{i}. {score}")
new_score = int(input("Input new score: "))
high_scores.append(new_score)
print("High scores:")
for i, score in enumerate(high_scores, start=1):
    print(f"{i}. {score}")
high_scores.sort(reverse=True)
print("High scores:")
for i, score in enumerate(high_scores, start=1):
    print(f"{i}. {score}")
