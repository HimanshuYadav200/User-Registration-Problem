import re
import logging

logging.basicConfig(filename="user_info.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def validate_user_name(first_name):
    """
    description: Function validates the first name of user.
    parameters: Function takes first name of user as a parameter.
    return: Function returns True if first name of user is valid and False if not valid.
    """
    try:
        logging.debug(f"received input for validation: {first_name}")
        
        pattern=r"^[A-Z].{2,}$"
        
        if not first_name:
            logging.critical("Empty username input detected")
            return False
        
        if not re.match(r"^.{3,}$",first_name):
            logging .error(f"username too short: {first_name}")
            return False
            
        if re.match(pattern,first_name):
            logging.info(f"Valid username: {first_name}")
            return True
        else:
            logging.warning(f"Invalid username attempt: {first_name}")
            return False  
    except Exception as e:
        logging.error(f"Error validating first name of user: {str(e)}")  

def validate_user_lastname(last_name):
    """
    description: Function validates the last name of user.
    parameters: Function takes last name of user as a parameter.
    return: Function returns True if last name of user is valid and False if not valid.
    """
    try:
        logging.debug(f"received input for validation: {last_name}")
        
        pattern=r"^[A-Z].{2,}$"
        
        if not last_name:
            logging.critical("Empty username input detected")
            return False
        
        if not re.match(r"^.{3,}$", last_name):
            logging .error(f"username too short: {last_name}")
            return False
            
        if re.match(pattern,last_name):
            logging.info(f"Valid username: {last_name}")
            return True
        else:
            logging.warning(f"Invalid username attempt: {last_name}")
            return False  
    except Exception as e:
        logging.error(f"Error validating last name of user: {str(e)}")  

def check_mail(mail_to_check):
    """
    description: Function validates the email of user.
    parameters: Function takes email of user as a parameter.
    return: Function returns True if email of user is valid and False if not valid.
    """
    try:
        logging.debug(f"Received mail for validation: {mail_to_check}")

        pattern = r'^[a-zA-Z0-9.+_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not mail_to_check:
            logging.critical(f"User input is empty")
            return False

        if re.match(pattern, mail_to_check):
            logging.info(f"Mail is valid: {mail_to_check}")
            return True
        else:
            logging.warning(f"{mail_to_check} is an invalid mail")
            return False  
    except Exception as e:
        logging.error(f"Error validating email: {str(e)}")

def check_mobile_format(number):
    """
    description: Function validates the mobile number format.
    parameters: Function takes mobile number as a parameter.
    return: Function returns True if mobile number is valid and False if not valid.
    """
    try:
        logging.debug(f"Input number {number} received for validation")
        
        pattern = r"^[0-9]{2}\s\d{10}$"
        
        if not number:
            logging.critical("Empty input for number detected")
            return False 

        if not re.match(r"^\d{2}\s\d{10}$", number):
            logging.error(f"Number {number} is incorrect in length")
            return False 

        if re.match(pattern, number):
            logging.info(f"Mobile number {number} is valid")
            return True 
        else:
            logging.warning(f"Mobile number {number} is invalid")
            return False 
    except Exception as e:
        logging.error(f"Error validating mobile number: {str(e)}")

def check_pass(pass_to_check):
    """
    description: Function validates the password length.
    parameters: Function takes password as a parameter.
    return: Function returns True if password meets length criteria and False if not.
    """
    try:
        logging.debug(f"received password {pass_to_check} for checking")
    
        pattern=r"^.{8,}$"
    
        if not pass_to_check:
            logging.critical("input password is empty")
            return False

        if re.match(pattern,pass_to_check):
            logging.info(f"password {pass_to_check} is valid")
            return True
        else:
            logging.warning(f"password {pass_to_check} is invalid")  
            return False
    except Exception as e:
        logging.error(f"Error validating password: {str(e)}")

def check_pass_uppercase(pass_to_check):
    """
    description: Function validates if password contains at least one uppercase letter.
    parameters: Function takes password as a parameter.
    return: Function returns True if criteria is met and False if not.
    """
    try:
        logging.debug(f"received password {pass_to_check} for checking")
    
        pattern=r"^(?=.*[A-Z]).{8,}$"
    
        if not pass_to_check:
            logging.critical("input password is empty")
            return False
        
        if not re.search(r"[A-Z]", pass_to_check):
            logging.error(f"Password '{pass_to_check}' does not contain an uppercase letter")
            return False

        if re.match(pattern,pass_to_check):
            logging.info(f"password {pass_to_check} is valid")
            return True
        else:
            logging.warning(f"password {pass_to_check} is invalid")  
            return False  
    except Exception as e:
        logging.error(f"Error validating password for uppercase letter: {str(e)}")

def check_pass_numeric(pass_to_check):
    """
    description: Function validates if password contains at least one numeric number.
    parameters: Function takes password as a parameter.
    return: Function returns True if criteria is met and False if not.
    """
    try:
        logging.debug(f"received password {pass_to_check} for checking")
    
        pattern=r"^(?=.*[A-Z])(?=.*\d).{8,}$"
    
        if not pass_to_check:
            logging.critical("input password is empty")
            return False
        
        if not re.search(r"[A-Z]", pass_to_check):
            logging.error(f"Password '{pass_to_check}' does not contain an uppercase letter")
            return False
        
        if not re.search(r"\d", pass_to_check):
            logging.error(f"Password '{pass_to_check}' does not contain a numeric number")
            return False

        if re.match(pattern,pass_to_check):
            logging.info(f"password {pass_to_check} is valid")
            return True
        else:
            logging.warning(f"password {pass_to_check} id invalid")  
            return False  
    except Exception as e:
        logging.error(f"Error validating password for numeric number: {str(e)}")

def check_pass_special_character(pass_to_check):
    """
    description: Function validates if password contains at least one special character.
    parameters: Function takes password as a parameter.
    return: Function returns True if criteria is met and False if not.
    """
    try:
        logging.debug(f"received password {pass_to_check} for checking")
    
        pattern=r"^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*]).{8,}$"
    
        if not pass_to_check:
            logging.critical("input password is empty")
            return False
        
        if not re.search(r"[A-Z]", pass_to_check):
            logging.error(f"Password '{pass_to_check}' does not contain an uppercase letter")
            return False
        
        if not re.search(r"\d", pass_to_check):
            logging.error(f"Password '{pass_to_check}' does not contain a numeric number")
            return False
        
        if not re.search(r"[@#$%^&*]", pass_to_check):
            logging.error(f"Password '{pass_to_check}' does not contain a special character")
            return False

        if re.match(pattern,pass_to_check):
            logging.info(f"password {pass_to_check} is valid")
            return True
        else:
            logging.warning(f"password {pass_to_check} id invalid")  
            return False  
    except Exception as e:
        logging.error(f"Error validating password for special_character: {str(e)}")
        
    
def main():
    initial_name=input("Enter first name: ")
    if validate_user_name(initial_name):
        print(f"{initial_name} is valid user name")
    else:
        print("invalid user name")  
    
    sur_name=input("Enter last name: ")
    if validate_user_lastname(sur_name):
        print(f"{sur_name} is valid user name")
    else:
        print("invalid user name")   
    
    email = input("Enter an email address: ")
    if check_mail(email):
        print(f"{email} is a Valid Email Address.")
    else:
        print(f"{email} is an Invalid Email Address.")
     
    mobile_num = input("Enter country code and mobile number: ")
    if check_mobile_format(mobile_num):
        print(f"{mobile_num} is a valid mobile number.")
    else:
        print("Invalid mobile number.")
    
    Password=input("Enter a password of minimum length 8: ")
    if check_pass(Password):
        print("Password is a Valid.")
    else:
        print("Password is Invalid.")     

    Password=input("Enter a password with length 8 and should have a upper case: ")
    if check_pass_uppercase(Password):
        print("Password is a Valid.")
    else:
        print("Password is Invalid.")     
  
    Password=input("Enter a password with length 8 and should contain uppercase and numeric number: ")
    if check_pass_numeric(Password):
        print("Password is a Valid.")
    else:
        print("Password is Invalid.")  
  
    Password=input("Enter a password with length 8 and should contain uppercase,numeric number and special character: ")
    if check_pass_special_character(Password):
        print("Password is a Valid.")
    else:
        print("Password is Invalid.")  
    
if __name__=="__main__":
    main()
    
  
  
  
    
    
        