# Read data from CSV files stored in a different directory than the current working directory
# For ease of use, create a 'PyData' directory in '\user\Documents' and change abs path to fit your machine
import pandas as pd
import os

target_directory = r'C:\Users\benca\Documents\PyData\MultiVariate'
reset_cwdir = os.getcwd()

if __name__ == "__main__":
    print(f'\nTarget Directory:\n{target_directory}\n'
          f'\nInitial Directory:\n{reset_cwdir}\n'
          f'\n~~~~~~~~~~~~~~~~~~~~~')
    while True:
        # Run get_data explicitly to search for and examine data sets
        try:
            os.chdir(target_directory)
            print(f'\nCurrent Working Directory: "{os.getcwd()}"\n{os.listdir()}\n')
            file_name = str(input("Enter file name for dataSet in PyData: "))
            chk_data = pd.read_csv(file_name, delimiter=',')
            os.chdir(reset_cwdir)
            print(f'\nData:\n{chk_data.head(10)}\n'
                  f'\nChecking')
            break
        except FileNotFoundError:
            print(f'\n!!! File search failed !!!\nMake sure directory path and file name are correct!'
                  f'\n------------------------------------------------')

else:
    while True:
        # Calling from another module eliminates the overhead for file examination
        # Displays CWD contents and prompts user for file name to import
        # Returns a numpy data object to program that called it
        try:
            os.chdir(target_directory)
            print(f'\nCurrent Working Directory: "{os.getcwd()}"\n{os.listdir()}\n')
            file_name = str(input("Enter file name for dataSet in PyData: "))
            data = pd.read_csv(f"{file_name}", delimiter=',').to_numpy()
            os.chdir(reset_cwdir)
            break
        except FileNotFoundError:
            print(f'\n!!! File search failed !!!\nMake sure directory path and file name are correct!'
                  f'\n------------------------------------------------')
