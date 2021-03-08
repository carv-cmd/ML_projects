# Read data from an external database
import pandas as pd
import os

if __name__ == "__main__":
    try:
        os.chdir(r'C:\Users\benca\Documents\PyData')
        print(f'\nCurrent Working Directory: {os.getcwd()}\n'
              f'\nCWD Contents:\n{os.listdir()}\n')
        file_name = str(input("Enter file name for dataSet in PyData: "))
        chk_data = pd.read_csv(f"{file_name}", delimiter=',')
        print(f'\nType(Data): {type(chk_data)}\n'
              f'\nData:\n{chk_data.head(10)}')

    except FileNotFoundError:
        print("\nFile search failed!\n")
        print(f'\nCurrent Working Directory: {os.getcwd()}')

else:
    try:
        os.chdir(r'C:\Users\benca\Documents\PyData')
        print(f'\nCurrent Working Directory: {os.getcwd()}\n'
              f'\nCWD Contents:\n{os.listdir()}\n')
        file_name = str(input("Enter file name for dataSet in PyData: "))
        data = pd.read_csv(f"{file_name}", delimiter=',').to_numpy()

    except FileNotFoundError:
        print("\nFile search failed!\n")
        print(f'\nCurrent Working Directory: {os.getcwd()}')


