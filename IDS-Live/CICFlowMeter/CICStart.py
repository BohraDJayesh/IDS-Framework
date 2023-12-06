import subprocess
import os
import csv
def startCIC(command):
    
    try:
        # This section will run the command by opening a seperate terminal specially for cicflowmeter to run properly
        applescript = f'tell application "Terminal" to do script "{command}"'
        subprocess.Popen(['osascript', '-e', applescript], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) #Trying to run it in seperate command.

    except subprocess.CalledProcessError as e:
        # Handle error if the command returns a non-zero exit code
        print("Error:", e)

def checkAndWriteCSV(path, name):
    if os.path.isfile(path) == 'False':
        with open(path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)


if __name__ == "__main__":
    CSVFileName = 'startFlow.csv'
    CSVFilePath = 'IDS-Live/CSV/'
    command = f" sudo cicflowmeter -i en0 -c /Users/jayeshduttbohra/Desktop/JD/Projects/IDS-Framework/IDS-Live/CSV/startFlow.csv"
    #Checking if the CSV exists or not, if not the function will create a new csv with that name and path.
    checkAndWriteCSV(CSVFilePath, CSVFileName)
    
    #Finally calling startCIC function to initiate the capturing process.
    startCIC(command)