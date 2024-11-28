def coin_change(coins, amount):
    # สร้างตาราง dp เก็บจำนวนน้อยสุดของเหรียญที่ต้องใช้สำหรับแต่ละจำนวนเงิน
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # ถ้าต้องการเงิน 0 บาท ไม่ต้องใช้เหรียญเลย
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # คำตอบคือ 3 (ใช้เหรียญ 5, 5, 1)
