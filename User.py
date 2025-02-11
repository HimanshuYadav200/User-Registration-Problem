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
    
    
        