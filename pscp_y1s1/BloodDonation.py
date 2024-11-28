"""BloodDonation problem via iJudge during pair programming"""
def is_donatable():
    """
    This function evaluates if one is eligible for blood donation

    Arguments:
    - Age (int): Age of a person
    - Weight (int): Weight of a person
    - History (int): Past history of donation
    - Permit (bool): (If age is below 17) True or False

    Returns:
    - Evaluation result (str): 'Yes' if a person is eligible for blood donation and vice versa

    Raises:
       None.
    """
    age = int(input())
    weight = int(input())
    history = int(input())
    if age == 17 or 60 <= age <= 70:
        aaa = input()
        permit = aaa == "True"

    else:
        permit = True

    old_enough = bool(17 <= age <= 70)
    weight = bool(weight >= 45)
    if history:
        history = True
    else:
        history = bool(age <= 55)
    if old_enough and weight and history and permit:
        print('Yes')
    else:
        print('No')
is_donatable()
