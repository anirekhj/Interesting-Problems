import sys
from itertools import combinations, chain
from collections import defaultdict

# Find nodes with odd-degrees
def findNonRepeating(arr, n):
  odd_appearances = []
  # Insert all array elements in hash
  # table
  mp={}
  for i in range(n):
      if arr[i] not in mp:
          mp[arr[i]]=0
      mp[arr[i]]+=1

  # Traverse through map only and
  for x in mp:
      if (mp[x]%2==1):
          odd_appearances.append(x)
  return odd_appearances;


def chop_strings(strings, k):
  res = []

  for string in strings:
    res.append([string[x:y] for x, y in combinations(range(len(string) + 1), r = 2) if len(string[x:y]) == k ])

  merged = list(chain.from_iterable(res))
  return list(set(merged));


def make_edges(strings, k):
  res = []

  for string in strings:
    res.append([string[x:y] for x, y in combinations(range(len(string) + 1), r = 2) if len(string[x:y]) == k ])

  return res;


def main():
  outpath=""
  strings = []
  # read input size from stdin
  size=int(sys.stdin.readline())

  # read input strings and store them in a list
  while(size):
    strings.append(sys.stdin.readline().strip())
    size = size-1

  # find the length of smallest input string
  k = len(min(strings, key=len))

  while (k > 1) {
    # get the substrings of k length from input strings
    # print(strings)
    chopped_set = chop_strings(strings, k);
    # print(sorted(chopped_set))
    # vertices = chop_strings(chopped_set, k-1);
    # print(sorted(vertices))
    edges = make_edges(chopped_set, k-1);

    terminal_points = findNonRepeating(list(chain.from_iterable(edges)),len(list(chain.from_iterable(edges))));

    # print(terminal_points)
    # print()
    # print(edges)
    terminal_index=""
    end_point=[]
    while (terminal_points):
      try:
        terminal_index = [row[0] for row in edges].index(terminal_points[0])
      except ValueError:
        if (terminal_points[0] in end_point):
          break;
        else:
          end_point.append(terminal_points[0])
          del terminal_points[0]

      if (terminal_index!=""):
        if (outpath==""):
          outpath = terminal_points[0] + edges[terminal_index][1][-1]
        else:
          outpath = outpath + edges[terminal_index][1][-1]
        terminal_points[0] = edges[terminal_index][1]
        del edges[terminal_index]
    print(outpath)
  }


main();
