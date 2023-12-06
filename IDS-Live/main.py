from tabnanny import verbose
import time
import os
import subprocess
import datetime
import logging
from subprocess import Popen
import pandas as pd
from CICFlowMeter.CICStart import startCIC , checkAndWriteCSV
from CICCSVLoader.csvFlowLoader import CSVFlowLoader
import mlstart
from Preprocessing.constants import PredictLabel, COLUMNS
import sys

CSVFileName = 'startFlow.csv'
CSVFilePath = 'CSV/'
command = f" sudo cicflowmeter -i en0 -c /Users/jayeshduttbohra/Desktop/JD/Projects/IDS-Framework/IDS-Live/CSV/startFlow.csv"
DATACLEAN_PIPELINE_FILEPATH = "Preprocessing/joblib_dumps/dataclean_pipeline.joblib"
DATAPREP_PIPELINE_FILEPATH = "Preprocessing/joblib_dumps/dataprep_pipeline.joblib"

def runIDS(verbose=False):
    
    dots = 0
    start_time = time.time()

    while time.time() - start_time < 5:
        sys.stdout.write("\rStarting" + "." * dots)
        sys.stdout.flush()
        dots = (dots + 1) % 4
        time.sleep(0.5)  # Adjust the sleep time as needed

    try:
        # Create log file if it does not exist.
        if not os.path.exists('logs/idslogs/ids.log'):
            file = open(os.path.join('logs/idslogs','ids.log'), 'w')
            file.close()
        logging.basicConfig(filename=os.path.join('logs/idslogs','ids.log'), level=logging.INFO)
        csvloader = CSVFlowLoader(os.path.join(CSVFilePath, CSVFileName))

        

        while True:
            for flowline in csvloader.tailFile():
                csValsArray = [list(flowline.split(","))]
                csValsDF = pd.DataFrame(csValsArray, columns=COLUMNS)

                #Sending to mlstart for preprocessing and prediction.
                csValsDF = mlstart.colPreprocessing(csValsDF)

                # Actual detection and printing results out in stdout.
                if mlstart.predict(csValsDF)[0] in PredictLabel.ANOMALY:

                    print("ANOMALY: %s" % (parsePredictionDF(csValsDF)))
                    logging.info("ANOMALY: %s" % (parsePredictionDF(csValsDF)))
                else:
                    if verbose:
                        print("BENIGN: %s" % (parsePredictionDF(csValsDF)))
    except KeyboardInterrupt:
        print("Exiting...")
        csvloader.destroy()

def parsePredictionDF(dataframe):
    src_ip = dataframe["Src IP"].values[0]
    src_port = dataframe["Src Port"].values[0]
    dst_ip = dataframe["Dst IP"].values[0]
    dst_port = dataframe["Dst Port"].values[0]
    timestamp = dataframe["Timestamp"].values[0]
    return "%s %s:%s => %s:%s" % (timestamp,src_ip, src_port, dst_ip, dst_port)


if __name__ == "__main__":

    checkAndWriteCSV(CSVFilePath,CSVFileName)
    startCIC(command)

    runIDS(verbose=True)


