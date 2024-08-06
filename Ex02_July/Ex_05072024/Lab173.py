# Wal IN dIR
import os

for root, dir, files in os.walk("/Users/Ankita Sharma/PycharmProjects/PyLearning3xATB/Ex02_July/Ex_05072024"):
    print(f"Current Dir {root}")
    print(f"Sub Dir Dir {dir}")
    print(f"files Dir Dir {files}")
    print(len(files))