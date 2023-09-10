import os
import time
import sys
import subprocess

def usage():
    print('python3 dictionary_mass_test.py', '<approach> <data fileName> <number of times to run>')
    print('<approach> = <array | linkedlist | trie>')
    sys.exit(1)

def main():
    args = sys.argv

    if len(args) != 4:
        print('Incorrect number of arguments.')
        usage()
    
    list_of_times = []
    for i in range(int(args[3])):
        start = time.time()
        subprocess.call(["python3", "dictionary_file_based.py", args[1], args[2], "test1.in", "test1.out"])
        end = time.time()

        time_taken = end - start
        print(f"time taken: {time_taken}")
        list_of_times.append(time_taken)
    
    sum_of_times = sum(list_of_times)
    average_of_times = sum_of_times / len(list_of_times)
    print(f"\naverage time taken: {average_of_times}")

if __name__ == "__main__":
    main()