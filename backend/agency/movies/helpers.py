from dateutil.parser import parse


def isValidPostRequest(data):
    '''Checks that the body of a create movie request is the correct format.
    Args:
        data (dict):  The request body
    Returns:
        bool: True if successfull.
    '''
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


def isValidDateString(iso_date):
    '''Checks that a date string is the correct format.
    Args:
        data (dict):  The request body
    Returns:
        bool: True if successfull.
    '''
    isValid = True
    try:
        validDate = parse(iso_date)
        if not validDate:
            isValid = False
    except Exception:
        isValid = False
    return isValid


def reformat(data):
    '''Reformats the release date key

       This function is used to convert the release date
       from using a hyphen (release-date),to using an
       underscore (release_date) which is the expected
       attribute of the Movie model as well as converting the iso date
       string to a datetime object.

       Args:
        data (dict):  The request body
       Returns:
        dict: The reformatted data.
       '''
    reformatted_data = {
        'title': data['title'],
        'release_date': parse(data['release-date'])
    }
    return reformatted_data


def isValidPatchRequest(data):
    '''Checks that the body of an edit movie request is the correct format.
    Args:
        data (dict):  The request body
    Returns:
        bool: True if successfull.
    '''
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


def isValidActorId(data):
    '''Checks that the actor ID passed in a request body is the correct format.
    Args:
        data (dict):  The request body
    Returns:
        bool: True if successfull.
    '''
    isValid = True
    if 'actor-id' not in data.keys() or data['actor-id'] == '':
        isValid = False
    if 'actor-id' in data.keys() and not isinstance(data['actor-id'], int):
        isValid = False
    return isValid
