def Median_Arrays(nums1, nums2):

  merged = []
  merged.extend(nums1)
  merged.extend(nums2)                      # O(m + n)

  k = len(merged)                           # O(1)

  for i in range(k):
    for j in range(0, k - i - 1):
      if merged[j] > merged[j + 1]:
        tmp = merged[j]
        merged[j] = merged[j + 1]
        merged[j + 1] = tmp                 # O(n**2)

  if k % 2 == 1:
    return merged[k // 2]                   # O(1)
  else:

    mid1 = merged[(k // 2) - 1]
    mid2 = merged[k // 2]
    return (mid1 + mid2) / 2                # O(1)

m = int(input("Enter The Elements Of The First List: "))
nums1 = []
for i in range(m):
  x = int(input(f"Enter number {i + 1}: "))
  nums1.append(x)

n = int(input("Enter The Elements Of The Second List: "))
nums2 = []
for i in range(n):
  y = int(input(f"Enter number {i + 1}: "))
  nums2.append(y)

print(Median_Arrays(nums1, nums2))