def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4

  for x in range(end):
    if nums[x] == 9:
      return True
  return False
