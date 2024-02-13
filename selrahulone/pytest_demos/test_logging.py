#its for logging purpose import logging
import logging
def test_loggingDemo():
    logger=logging.getLogger(__name__) # here[__name__] give the testcase name

    filehandler=logging.FileHandler("logs.log") #its identify the place of the testcases location their gives

    #below formatter about in logs its give strecture
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

    #below one display the output
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler) # its create the connection to filehandler(filehandler obj)


    logger.setLevel(logging.DEBUG) # here pass the which one you need to pass here
    logger.info("its info details related")
    logger.warning("its shows the warning ")
    logger.error("its shows the error")
    logger.critical("its shows the critical")
    logger.debug("its show the debug related details")



