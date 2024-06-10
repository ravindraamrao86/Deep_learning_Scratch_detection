import sys
import logging

def error_message_deatil(error,error_deatil:sys):

    _,_,exc_tb= error_deatil.exc_info()
    file_name =exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number[{1}] error_message[{2}]".format(
    file_name,exc_tb. tb_lineno,str(error) )

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_deatil:sys): 
        super().__init__(error_message)
        self.error_message=error_message_deatil(error_message,error_deatil=error_deatil)
    
    def __str__(self):        
        return self.error_message 
    
if __name__ == "__main__":  # type: ignore

    try:
        a= 1/0
    except Exception as e :
        
        raise CustomException(e,sys)        
