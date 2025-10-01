"""
CP1404/CP5632 - Practical
Random Numbers
"""

# What did you see on line 1?
# 16
# What was the smallest number you could have seen, what was the largest?
# 5, 20

# What did you see on line 2?
# 9
# What was the smallest number you could have seen, what was the largest?
# 3, 9
# Could line 2 have produced a 4?
# No, the randrange statement starts at 3 and has a step of 2, so 4 is skipped when it is executed.

# What did you see on line 3?
# 3.9455102270430356
# What was the smallest number you could have seen, what was the largest?
# 2.5, 5.5

import random

print(random.randint(1, 100))
