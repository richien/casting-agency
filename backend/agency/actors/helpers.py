from agency.movies.helpers import isValidDateString


def isValidPostRequest(data):
    expected_fields = [
        'name',
        'dob',
        'gender'
    ]
    isValid = True
    for field in expected_fields:
        if field not in data.keys() or data[field] == "":
            isValid = False
        if field == 'dob' and field in data.keys():
            if not isValidDateString(data[field]):
                isValid = False
    return isValid


def isValidPatchRequest(data):
    updateable_fields = [
        'name',
        'dob',
        'gender'
    ]
    isValid = True
    for field in data.keys():
        if data[field] == "":
            isValid = False
        if field not in updateable_fields:
            isValid = False
        if field == 'dob' and not isValidDateString(
                                            data[field]):
            isValid = False
    return isValid
