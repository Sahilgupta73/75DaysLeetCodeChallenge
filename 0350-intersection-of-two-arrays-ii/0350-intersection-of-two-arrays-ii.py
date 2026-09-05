class Solution(object):

  def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # Swap so nums1 is always the smaller array to optimize space
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1

    # Count frequencies of elements in the smaller array
    counts = {}
    for num in nums1:
      counts[num] = counts.get(num, 0) + 1

    result = []
    # Collect matching elements
    for num in nums2:
      if counts.get(num, 0) > 0:
        result.append(num)
        counts[num] -= 1

    return result