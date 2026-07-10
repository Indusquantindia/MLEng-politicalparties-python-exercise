Write a recursive function to flatten a deeply nested list of integers. The depth is unknown.
Input: [1, [2, [3, 4], 5], 6, [7, 8]]
Output: [1, 2, 3, 4, 5, 6, 7, 8]
 
Here is a recursive function to flatten a deeply nested list of integers:
```python
def flatten(nested_list):

df = [1, [2, [3, 4], 5], 6, [7, 8]]
