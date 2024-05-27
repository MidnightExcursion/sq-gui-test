_USER_RESPONSE_APPROVED = 'y'
_USER_RESPONSE_DECLINED = 'n'

_ACCEPTABLE_USER_RESPONSES = [
    _USER_RESPONSE_APPROVED,
    _USER_RESPONSE_DECLINED
]

def acquire_user_authorization_to_set_up_directory_structure():
    """
    # Description:
    Obtain explicit (usually command-line) "authorization" from
    the user to set up a given directory structure. This is a 
    blocking function, which means that the user won't be able 
    to proceed evaluating the program until an input is collected.

    # Arguments:
    None

    # Returns:
    user_response_as_boolean: (bool)
    """

    user_response_as_boolean = False

    while True:

        try:

            user_response = str(input("> You are about to create a new directory structure on your machine. Do you approve this action? ['Y', 'N']"))
        
        except ValueError:
            
            print(f"> Provided input could not be coerced to StringType. Please try again.")
            continue
        
        if user_response.lower() in _ACCEPTABLE_USER_RESPONSES:

            if user_response.lower() ==_USER_RESPONSE_DECLINED:

                print(f"> User declined to create necessary directory structure. Exiting...")
                user_response_as_boolean = False
                break

            elif user_response.lower() == _USER_RESPONSE_APPROVED:

                print(f"> User accepted to create directory structure.")
                user_response_as_boolean = True
                break
            
            else:

                print(f"> Did not understand input {user_response}. How did you get here?")
                continue

        else:

            print(f"> Did not understand input {user_response}. Give an acceptable response. ['Y', 'N']")
            continue

    return user_response_as_boolean