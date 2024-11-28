""" TakingTurn """
import json

def alternate_list(lst):
    """ sd """
    result = []
    left = 0
    right = len(lst) - 1


    if left <= right:
        result.append(lst[right])
        right -= 1


    if left <= right:
        pattern = ['right', 'right', 'left', 'left']
        index = 0  # ตำแหน่งใน pattern
        while left <= right:
            if pattern[index] == 'right' and left <= right:
                result.append(lst[right])  # เลือกจากฝั่งขวา
                right -= 1
            elif pattern[index] == 'left' and left <= right:
                result.append(lst[left])  # เลือกจากฝั่งซ้าย
                left += 1
            # เปลี่ยนตำแหน่งใน pattern และวนซ้ำเมื่อครบ 4 ขั้นตอน
            index = (index + 1) % len(pattern)

    return result


print(alternate_list(json.loads(input())))
