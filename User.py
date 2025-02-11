import re
import logging

logging.basicConfig(filename="sample.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def validate_user_name(first_name):
    
    logging.debug(f"received input for alidation: {first_name}")
    
    pattern=r"^[A-Z].{2,}$"
    
    if not first_name:
        logging.critical("Empty username input detected")
        return False
    
    if len(first_name)<3:
        logging .error(f"username too short: {first_name}")
        return False
        
    if re.match(pattern,first_name):
        logging.info(f"Valid username: {first_name}")
        return True
    else:
        logging.warning(f"Invalid username attempt: {first_name}")
        return False  
    


def validate_user_lastname(last_name):
    
    logging.debug(f"received input for validation: {last_name}")
    
    pattern=r"^[A-Z].{2,}$"
    
    if not last_name:
        logging.critical("Empty username input detected")
        return False
    
    if len(last_name)<3:
        logging .error(f"username too short: {last_name}")
        return False
        
    if re.match(pattern,last_name):
        logging.info(f"Valid username: {last_name}")
        return True
    else:
        logging.warning(f"Invalid username attempt: {last_name}")
        return False  
    
    


def check_mail(mail_to_check):
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





def check_mobile_format(number):
    logging.debug(f"Input number {number} received for validation")
    
   
    pattern = r"^[0-9]{2}\s\d{10}$"
    
    if not number:
        logging.critical("Empty input for number detected")
        return False 

    if len(number) != 13:
        logging.error(f"Number {number} is incorrect in length")
        return False 

    if re.match(pattern, number):
        logging.info(f"Mobile number {number} is valid")
        return True 
    else:
        logging.warning(f"Mobile number {number} is invalid")
        return False 
 
    
    
    


    
    
if __name__=="__main__":
    
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
    
    
        