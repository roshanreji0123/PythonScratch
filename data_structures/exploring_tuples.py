#exploring_tuples.py
if __name__ == "__main__":
    t_uple = (1, 2, 3, 4, 2)
    print(f"Tuple: {t_uple}")
    print(f"Occurrences of 2: {t_uple.count(2)}")#counts the occurence of 2 in the tuple
    print(f"Index of 1: {t_uple.index(1)}")#returns the index of 1

    total = sum(t_uple)#sum of elements in the tuple
    avg = total / len(t_uple)# length of tuple using len(t_uple)
    print(f"Sum: {total}")
    print(f"Average: {avg}")

