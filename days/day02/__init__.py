# Advent of Code 2023 - Day 02
# https://adventofcode.com/2023/day/2
#
# solution by gretchen.keppel@gmail.com


# ==========================================================================
class Day01:
  def __init__(self,dataset):
    self.data = dataset
    self.result1 = None
    self.result2 = None

  # docstring
  def part1(self, data=None):
    result=0
    return result
      
  # docstring
  def part2(self):
    result=0
    return result
    

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
  fpath = "./test1.txt" # this is the sample dataset.
  P = Day01(fetch(fpath))
  assert 0 == P.part1(), "Part 1: Should be 0"
  
  fpath = "./test1.txt" # this is the sample dataset.
  P = Day01(fetch(fpath))
  assert 0 == P.part2(), "Part 2: Should be 0."
  
  fpath = "./input.txt" # this is the live dataset.
  P = Day01(fetch(fpath))
  r1 = P.part1()
  r2 = P.part2()

  result = {
    "Part 1" : r1,
    "Part 2" : r2
  }

  return result


# ==========================================================================
if __name__ == "__main__" :
  result = main()
  print(result)

