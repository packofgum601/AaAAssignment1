import os
import time
import sys

def usage():
    print('python3 dictionary_mass_test.py', '<approach> <data fileName> <number of times to run>')
    print('<approach> = <array | linkedlist | trie>')
    sys.exit(1)

def main():
    args = sys.argv

    if len(args) != 4:
        print('Incorrect number of arguments.')
        usage()
    
    """
    - Run file x number of times
    - Record start time
    - Record end time
    - Calculate average
    """
    
    list_of_times = []
    for i in range(int(args[3])):
        start = time.process_time_ns()
        os.system(f'python3 dictionary_file_based.py {args[1]} {args[2]} test1.in test1.out')
        end = time.process_time_ns()

        time_taken = end - start
        print(f"time taken: {time_taken}")
        list_of_times.append(time_taken)
    
    sum_of_times = sum(list_of_times)
    average_of_times = sum_of_times / len(list_of_times)
    print(f"\naverage time taken: {int(average_of_times)}ns")

if __name__ == "__main__":
    main()