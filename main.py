# importing the module
import timeit

# code segment to measure
code_segment = """\
import random
def execute(n):
	return n**n
execute(random.randint(20, 50))
"""

# execute code segment and find the execution time
exec_time = timeit.timeit(code_segment, number=10**6)

# printing the execution time in secs.
# nearest to 3-decimal places
print(f"{exec_time:.03f} secs.")
