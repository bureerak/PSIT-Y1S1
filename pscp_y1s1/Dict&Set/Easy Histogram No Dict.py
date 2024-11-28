"Easy Histogram No Dict"
def histogram():
    "Easy Histogram No Dict"
    text = input()
    a_z = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    for i in a_z:
        if i in text:
            print(f"{i} = {text.count(i)}")
histogram()
