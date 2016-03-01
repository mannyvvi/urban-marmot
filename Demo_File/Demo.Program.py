import demo_logger
import demo_reader

prod = raw_input("Would you like to run the logger or reader? ",)
if prod == "logger":
    demo_logger.logger()
elif prod =="reader":
    demo_reader.reader()
    




