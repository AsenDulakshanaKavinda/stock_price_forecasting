import sys
import logging

def error_message_datails(error: Exception, error_detail: sys) -> str:

    exc_type, exc_value, exc_traceback = error_detail.exc_info()

    file_name = exc_traceback.tb_frame.f_code.co_filename

    line_number = exc_traceback.tb_lineno

    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    logging.error(error_message)

    return error_message


class ProjectException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_datails(error_message, error_detail)

    def __str__(self):
        return self.error_message












