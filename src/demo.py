import sys
import logging
from exception import ProjectException


# test exception + logger
def test_project_exception():
    app_logger = logging.getLogger("app")
    try:
        # Simulate an error
        result = 1 / 0  # Will raise ZeroDivisionError
    except ZeroDivisionError as e:
        app_logger.info("Testing ProjectException")
        raise ProjectException("Division by zero error", sys)

if __name__ == "__main__":
    # Run logging test
    print("Running test_log...")

    # Run exception test
    print("\nRunning test_project_exception...")
    try:
        test_project_exception()
    except ProjectException as e:
        print(f"Caught ProjectException: {e}")