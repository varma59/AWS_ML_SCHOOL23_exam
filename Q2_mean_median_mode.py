from statistics import mean, median, mode
class Result(object):
def __init__(self, arg1, arg2, arg3 self.output1 = arg1 # double
self.output2 = arg2 # double
self.output3 = arg3 # int
class UserMainCode(object):
@classmethod
def mmm(cls, input1, input2): # Calculate mean, median, and mode mean_value = round(mean(input2), 6) sorted_input2 = sorted(input2)
n = len(sorted_input2)
if n % 2 == 0:
median_value = round((sorted_input2[n // 2 = 1] + sorted_input2[n // 2]) / 2, 6)
else:
median_value = round(sorted_input2[n // 21, 6)
mode_value = mode(sorted_input2)
return Result(mean value, median_value, mode_value)
):
