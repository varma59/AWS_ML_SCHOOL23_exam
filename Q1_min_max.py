class UserMainCode(object):
@classmethod
def minimumCost(cls, input1, input2):
# Initialize an array to store the minimum cost to reach each city.
min_cost = [float('inf')] * input1
# The minimum cost to reach the first city is 0. min_cost[0] = 0
for i in range(input1):
# Check if there is a flight to city (i+1) and calculate the cost.
if i + 1 <input1: min_cost[i + 1] = min(min_cost[i + 1], min_cost[i] + abs(input2[i] - input2[i + 1]))
# Check if there is a flight to city (i+3) and calculate the cost.
if i + 3 < input1: min_cost[i + 3] = min(min_cost[i + 3], min_cost[i] + abs(input2[i] - input2[i + 3]))
# The minimum cost to reach the last city (city N) is the answer. return min_cost[-1]
