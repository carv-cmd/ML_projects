from make_dataSets import train_set
import os

reset = os.getcwd()


####################################################
####################################################
def define_dir(yes_save):
    """ Determines directory which to save .csv file in """
    to_my_cwd = str(input("\nSave in the Current Working Directory (y/n): "))
    file_name = str(input('\nDatSet Name: '))
    if to_my_cwd in yes_save:
        train_set.to_csv(f'{file_name}.csv')
    else:
        while True:
            try:
                target_dir = str(input("\nEnter Full Path to Target Directory: "))
                os.chdir(target_dir)
                train_set.to_csv(f'{file_name}.csv')
                os.chdir(reset)
                break
            except FileNotFoundError or NotADirectoryError:
                print("\nERROR: Please Check Directory Name!")
    return


####################################################
def save_function():
    """ Prompts user if they wish to save dataSet """
    yes_save = ['yes', 'y', 'yes ', 'ys', 'ye', 'es']
    while True:
        user_input = str(input("\nSave dataSet for future use? (y/n): ")).lower()
        if user_input not in yes_save:
            break
        else:
            define_dir(yes_save)
            break
    return


if __name__ == "__main__":
    save_function()
