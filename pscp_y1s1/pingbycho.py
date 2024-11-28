""" cho-chan """
def star():
    """ reply """
    _,_,c = input(),input(),input()
    use_a,use_b,use_c,use_d = input(),input(),input(),input()
    rec,time,high,low = 0,0,0,0
    for i in (use_a,use_b,use_c,use_d):
        if i.find("from") != -1:
            rec += 1
            if (i.find("time=")) == -1:
                milli=0
            else:
                milli=int(i[i.find("time")+5:i.find("ms")])
            time += milli
            if milli>high:
                high=milli
            if not low or milli<low:
                low=milli
    c = c[c.find("with")-1::-1].strip().replace("[","")
    c = c[:c.find(" ")].replace("]","")
    c = c[::-1]
    print(f"Ping statistics for {c}:")
    print(f"    Packets: Sent = 4, Received = {rec}, Lost = {4-rec} ({25*(4-rec)}% loss),")
    if rec:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {low}ms, Maximum = {high}ms, Average = {time//rec}ms")
star()
