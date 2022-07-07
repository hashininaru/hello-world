# eg.2.0.1 sorted with key, via def

v = ['Alice', 'Bob', 'Eve', 'Mallory']
def sort_key(x):
    return len(x)
sorted(v, key=sort_key)
