# Advent of Code 2023 - Day 01
# https://adventofcode.com/2023/day/1
#
# solution by gretchen.keppel@gmail.com


# ==========================================================================
class Day01:
  def __init__(self,dataset):
    # groups of numbers are separated by a blank record
    self.data = dataset
    self.totals = [0]
    self.result1 = None
    self.result2 = None

  # find the first and last integer in a string of characters, convert to a number, 
  # then return the sum of the full list
  def part1(self):
    alpha = []
    for row in self.data:
      alpha.append(''.join([char for char in row if char.isdigit()]))

    beta = [int(''.join([row[0],row[-1]])) for row in alpha]
    result = sum(beta)
    return(result)
      
  def part2(self):
    return 0


# --------------------------------------------------------------------------
# pull the dataset from a file 
def fetch(fpath):
  dataset = []
  
  with open(fpath, "r") as infile:
    dataset = [line.strip(" \n\r") for line in infile.readlines()]
        
  return dataset


# --------------------------------------------------------------------------  
# solve the problems.
def solve(dataset):
  p = Day01(dataset)

  p.part1()
  p.part2()

  return (p.result1, p.result2)  


# --------------------------------------------------------------------------
# do the main 
def main():
  fpath = "./test.txt" # this is the sample dataset.
  P = Day01(fetch(fpath))
  assert 142 == P.part1(), "Part 1: Should be 142"
  
  
  fpath = "./input.txt"
  P = Day01(fetch(fpath))
  r1 = P.part1()

  result = {
    "Part 1" : r1,
#    "Part 2" : r2
  }

  return result


# ==========================================================================
if __name__ == "__main__" :
  result = main()
  print(result)

