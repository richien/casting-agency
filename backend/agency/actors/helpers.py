
def isValidPostRequest(data):
    expected_fields = [
        'name',
        'age',
        'gender'
    ]
    isValid = True
    for field in expected_fields:
        if field not in data.keys() or data[field] == "":
            isValid = False
    return isValid


def isValidPatchRequest(data):
    updateable_fields = [
        'name',
        'age',
        'gender'
    ]
    isValid = True
    for field in data.keys():
        if data[field] == "":
            isValid = False
        if field not in updateable_fields:
            isValid = False
    return isValid
