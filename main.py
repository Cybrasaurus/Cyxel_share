import Functions as cy_f
import case_handling
import logging
import traceback
#logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logging.basicConfig(level=logging.INFO, format="%(message)s")
def main_loop():

    logging.info("Starting up")
    logging.info("Current Operation: Loading Main Config:")
    main_config = cy_f.Config_Reading.config_loader("config_main")
    logging.info("      Done")

    logging.info("\nCurrent Operation: Handling Config Files declared in main_config")
    for items in main_config["Files_To_Read"]:
        logging.info(f"     Now handling file: {items}")
        sub_config = cy_f.Config_Reading.config_loader(items)
        case_handling.auto_run_config(config_data=sub_config)

# Press the green button in the gutter to run the script.
def debug_wrap():
    try:
        main_loop()
    except Exception as exception:
        logging.critical(f"WARNING! PROGRAMM HAS CRASHED \nThis console will remain open until you close it")
        logging.critical(f"Error Message: {exception}")
        input("")
if __name__ == '__main__':
    main_loop()
    #debug_wrap()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# todo update word docu for kaufland
