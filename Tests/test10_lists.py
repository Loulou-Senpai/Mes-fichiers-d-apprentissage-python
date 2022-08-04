
import statistics

notes = [
    8, 12, 10, 9, 4, 20, 14
]
print(notes)
print(notes[0])
# Module stats
result = statistics.mean(notes)
print("La moyenne est de {}".format(result))