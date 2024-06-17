# สร้างฟังก์ชันเพื่อตรวจสอบสกิลที่ Invoker จะปล่อยออกมา
def check_spell(invoker, spell):
    if spell == 'Q':
        return 'COLD SNAP'
    elif spell == 'W':
        return 'GHOST WALK'
    elif spell == 'E':
        return 'ICE WALL'
    elif spell == 'R':
        if invoker.count('Q') >= 2 and invoker.count('W') >= 1 and invoker.count('E') >= 1:
            return 'CATACLYSM BOOM !!!'
        else:
            return None
    elif spell == 'S':
        if 'S' in invoker:
            return check_spell(invoker.replace('S', '', 1), 'S')
        else:
            return None
    elif spell == 'D':
        if 'D' in invoker:
            return check_spell(invoker.replace('D', '', 1), 'D')
        elif 'S' in invoker:
            return check_spell(invoker.replace('S', '', 1), 'S')
        else:
            return None

# อ่านอินพุต
invoker = input().strip()

# ตรวจสอบสกิลที่ Invoker จะปล่อยออกมา
result = []
for spell in invoker:
    spell_result = check_spell(invoker, spell)
    if spell_result:
        result.append(spell_result)

# พิมพ์ผลลัพธ์
if result:
    print(' '.join(result))
else:
    print('EZ MID')
