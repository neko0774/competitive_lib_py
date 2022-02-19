inf = 10**18


def merge(array, left, mid, right):
  L = array[left:mid]+[inf]
  R = array[mid:right]+[inf]
  l = 0
  r = 0

  for i in range(left, right):
    if L[l]<=R[r]:
      array[i] = L[l]
      l += 1
    else:
      array[i] = R[r]
      r += 1

def MergeSort(array, left=0, right=None):
  if right==None:
    right = len(array)
  if left+1<right:
    mid = (left+right)//2
    MergeSort(array, left, mid)
    MergeSort(array, mid, right)
    merge(array, left, mid, right)

import random as rd

def test():

  A = [rd.randint(0, 15) for _ in range(10)]
  print(A)
  MergeSort(A)


def main():
  N = int(input())
  A = [int(i) for i in input().split()]

  MergeSort(A)
  print(*A)
main()