import os 
import random

jenny_dir = "/Users/adaezeadigwe/Desktop/Edinburgh/Projects/CtrlSynSamples/JennySamples"


for sentfolder in os.listdir(jenny_dir):
    sentfolderpath = os.path.join(jenny_dir, sentfolder)
    files_in_folder = [os.path.join(sentfolder, fn) for fn in os.listdir(sentfolderpath)]
    print(files_in_folder)
    print('\n')
    list_of_fours = random.sample(files_in_folder, k=4)
    for audiochoice in list_of_fours:
        print(f'<audio controls><source src="https://aadigwe.github.io/CtrlSynSamples/JennySamples/{audiochoice}" type="audio/wav"> Your browser does not support the audio element.</audio>')
    input()