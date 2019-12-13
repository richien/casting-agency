from datetime import datetime


def isValidPostRequest(data):
    expected_fields = [
        'title',
        'release-date'
    ]
    isValid = True
    for field in expected_fields:
        if field not in data.keys():
            isValid = False
            break
        if field == 'title' and data[field] == '':
            isValid = False
            break
        if field == 'release-date'and not isValidDateString(
                                            data[field]):
            isValid = False
            break
    return isValid


def isValidDateString(date):
    isValid = True
    try:
        datetime.fromisoformat(date)
    except Exception:
        isValid = False
    return isValid


def reformat(data):
    """This function is used to convert the release date
       from using a hyphen (release-date) ,
       to using an underscore (release_date) which is the expected
       attribute of the Movie model as well as converting the iso date
       string to a datetime object."""
    reformatted_data = {
        'title': data['title'],
        'release_date': datetime.fromisoformat(data['release-date'])
    }
    return reformatted_data


def isValidPatchRequest(data):
    updateable_fields = [
        'title',
        'release-date'
    ]
    isValid = True
    for field in data.keys():
        if field not in updateable_fields:
            isValid = False
            break
        if field == 'release-date' and not isValidDateString(
                                                data[field]):
            isValid = False
            break
        if field == 'title' and data[field] == '':
            isValid = False
            break
    return isValid
