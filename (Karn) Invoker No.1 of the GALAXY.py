"""3star"""
def skill_recog(orb):
    """skill recognizer"""
    q_orb = orb.count("Q")
    w_orb = orb.count("W")
    e_orb = orb.count("E")

    if q_orb == 3:
        skill="COLD_SNAP"
    elif q_orb == 2 and w_orb == 1:
        skill="GHOST_WALK"
    elif q_orb == 2 and e_orb == 1:
        skill="ICE_WALL"
    elif w_orb == 3:
        skill="E.M.P"
    elif w_orb == 2 and q_orb == 1:
        skill="TORNADO"
    elif w_orb == 2 and e_orb == 1:
        skill="ALACRITY"
    elif e_orb == 3:
        skill="SUN_STRIKE"
    elif e_orb == 2 and q_orb == 1:
        skill="FORGE_SPIRIT"
    elif e_orb == 2 and w_orb == 1:
        skill="CHAOS_METEOR"
    elif q_orb == 1 and w_orb == 1 and e_orb == 1:
        skill="DEFEANING_BLAST"
    else:
        skill="EZ MID"
    return skill

def skill_check():
    """skill container and skill combination"""
    inskill = input()
    lskill = inskill
    lskill = lskill.replace("S","")
    lskill = lskill.replace("D","")
    lenght = len(inskill)
    variant = ""

    skill_sslot = ""
    skill_dslot = ""
    ans=""
    count_s = 0
    for i in range(lenght):
        if count_s == 1:
            count_s-=1
            continue

        if inskill[i] == "R":
            combo = lskill.find("R")
            if combo>2:
                contain = lskill[combo-1::-1]
                contain = contain[:3]
                lskill = contain[::-1]+lskill[combo+1:]
                variant = contain
                if not skill_sslot and skill_recog(variant) != "EZ MID":
                    skill_sslot = skill_recog(variant)
                elif skill_recog(variant) not in skill_sslot and skill_recog(variant)!="EZ MID":
                    skill_dslot = skill_sslot
                    skill_sslot = skill_recog(variant)
                continue
            lskill=lskill.replace("R","",1)

        if inskill[i] == "S" and skill_sslot:
            test=inskill+"*"
            if skill_sslot == "SUN_STRIKE" and test[i+1]=="S":
                ans+=" CATACLYSM_BOOM_!!!"
                count_s+=1
                continue
            ans+=f" {skill_sslot}"

        if inskill[i] == "D" and skill_dslot:
            test=inskill+"*"
            if skill_dslot == "SUN_STRIKE" and test[i+1]=="D":
                ans+=" CATACLYSM_BOOM_!!!"
                count_s+=1
                continue
            ans+=f" {skill_dslot}"
    ans=ans.strip()
    if ans:
        print(ans.strip().replace(" ",", ").replace("_"," "))
    else:
        print("EZ MID")
skill_check()
