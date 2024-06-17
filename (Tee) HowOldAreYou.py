"""How old He is"""
def main():
    """Main function"""
    d_1 = int(input())
    m_1 = int(input())
    y_1 = int(input())
    d_2 = int(input())
    m_2 = int(input())
    y_2 = int(input())
    if y_1 > y_2:
        print("Error")
    elif y_1 == y_2:
        if m_2 > m_1:
            print(f"{y_2-y_1}")
        elif m_2 == m_1:
            if d_2 >= d_1:
                print(f"{y_2-y_1}")
            else:
                print("Error")
        elif m_2 < m_1:
            print("Error")
    elif m_2 == m_1 :
        if d_2 >= d_1:
            print(f"{y_2-y_1}")
        else:
            print(f"{(y_2-y_1)-1}")
    elif m_2 > m_1:
        print(f"{y_2-y_1}")
    elif m_2 < m_1:
        print(f"{(y_2-y_1)-1}")
main()
