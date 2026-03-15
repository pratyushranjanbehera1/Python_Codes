print("Demostration of break statement")
for i in range(1,11):
    if i==5:
        print("abnormal Termination")
        break
    print(i)
print("Demostration of continue statement")
for i in range(1,11):
    if i==5:
        print("Skip Some portion of the loop")
        continue
    print(i)
