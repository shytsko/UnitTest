from typing import Sequence


class MaxNumberModule:
    @staticmethod
    def max_number(nums: Sequence[int]) -> int:
        if len(nums) == 0:
            raise ValueError

        max_num = None
        for num in nums:
            if max_num is None or num > max_num:
                max_num = num

        return max_num
