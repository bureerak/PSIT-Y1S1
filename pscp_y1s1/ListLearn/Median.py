""" Median """
def main(num = int(input())):
    """ function main """
    null = sorted([float( input() ) for _ in range(num)])
    posit = null[(int((num+1)/2)-1)] if (num+1)/2 == int((num+1)/2) else \
(null[int((num+1)/2) - 1] + null[int((num+1)/2)]) / 2
    print(f"{posit:.3f}")
main()
