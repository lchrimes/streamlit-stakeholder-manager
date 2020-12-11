import base64

def file_to_base64(fileName):
    """
    Opens a file and returns a base64 encoded file 
    """

    with open(fileName, 'rb') as f:
        fileBytes = f.read()
        base64File = base64.b64encode(fileBytes).decode('utf-8')

    return base64File

def bytes_to_base64(file):
    base64File = base64.b64encode(file).decode('utf-8')
    return base64File

def base64_to_bytes(file):
    fileBytes = base64.b64decode(file)
    return fileBytes