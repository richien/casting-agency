
def isValidActor(data):
    expected_fields = [
        'name',
        'age',
        'gender'
    ]
    isValid = True
    for field in expected_fields:
        if field not in data.keys():
            isValid = False
    return isValid
