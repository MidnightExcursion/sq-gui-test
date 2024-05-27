import os 

def create_folder(folder_name: str = "default_folder_name") -> bool:
    """
    # Description:
    Creates a folder by the name `folder_name` in a given directory.

    # Arguments:
    folder_name: (str)

    # Returns:
    (bool)
    """
    if folder_name == None:
        print(f"> Supplied argument for folder name was NoneType. Exiting...")
        return False
    
    if os is not None:
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
                print(f"> Created folder {folder_name}.")
                return True
            except:
                print(f"> ERROR: Unable to make new folder.")
                return False
        else:
            print(f"> Folder already exists.")
            return True
    else:
        print(f"> ERROR: unusual issue importing OS.")
        return False
    
def find_folder(folder_name: str = "default_folder_name") -> bool | None:
    """
    # Description:
    Attempt to find a folder. Will return the folder
    if it exists; otherwise, will return None.

    # Arguments:
    folder_name: (str)

    # Returns:
    bool | None
    """
    if folder_name == None:
        print(f"> Supplied argument for folder name was NoneType. Exiting...")
        return None

    if os is not None:
        return os.path.join(os.getcwd(), folder_name)
    else:
        print(f"> ERROR: unusual issue importing OS.")
        return None
