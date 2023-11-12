import  string
def encrypt(message: str, shift_by:int = 1):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char)+shift_by] if len(abc) >(abc.find(char)+shift_by) else abc[0] for id, char in enumerate(message)])
    return encrypted_message