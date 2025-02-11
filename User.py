import re
import logging

logging.basicConfig(filename="firstname_validation.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def validate_user_name(first_name):
    
    logging.debug(f"received input for validation: {first_name}")
    
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
    
    


    
    
if __name__=="__main__":
    initial_name=input("Enter first name: ")
if validate_user_name(initial_name):
    print(f"{initial_name} is valid user name")
else:
    print("invalid user name")  
    
    
        