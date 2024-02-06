import os 

head_html = ' \
<head> \
    <title>Ctrl FS2 Synthesis</title> \
     </head> '
feat_fullnames_dict = {'pa':'Pitch Average', 'pr': 'Pitch Range', 'pd' : "Average Phone Duration", 'se': 'Speech Energy', 'st': 'Spectral Tilt', 'f0std': 'Pitch Std', 'all': 'All Features'}


def arrange_table_cells(wav_directory, ctrl_values, sentence_id):
    wav_files_dict = {}
    
    for feat in features:
        feat_ctrl_wavpath = {value: "" for value in ctrl_values}
        for folder in os.listdir(wav_directory):
            if feat in folder:
                fullfolderpath = os.path.join(wav_directory, folder)
                fldr_control = fullfolderpath.split('_')[-1]
                for key in feat_ctrl_wavpath:
                    if key == fldr_control:
                        feat_ctrl_wavpath[key] = fullfolderpath +'/' +  sentence_id

        wav_files_dict[feat] = feat_ctrl_wavpath

    return wav_files_dict


def generate_html_page(wav_filepath_dict, ctrl_values, speaker):
    control_values = []

    with open(outputfile, "a") as file:
        file.write("<h4>"+speaker + "</h4>" + '<br />')
        file.write('<table>')
    
        # TABLE HEADING
        file.write('<tr>')
        file.write('<th>Feature</th>')
        for value in ctrl_values:
            file.write('<th>'+value+'</th>')
        file.write('</tr>')

        # WRITE ROWS
        for key in wav_filepath_dict:
            file.write('<tr>')
            file.write('<td>'+ feat_fullnames_dict[key] +'</td>')

            for value in ctrl_values:
                file_wavpath = wav_filepath_dict[key][value]
                file.write('<td> <audio controls=""><source src='+ file_wavpath + ' type="audio/wav"></audio> </td>')
                #Debug
                #file.write('<td>'+ wav_filepath_dict[key][value] +'</td>')

            file.write('</tr>')


        file.write('</table>')
        file.write('<br />')
        file.write('<hr />')
        file.write('<br />')

def generate_html_page_variation(wav_filepath_dict, ctrl_values, speaker):
    control_values = []

    with open(outputfile, "a") as file:
        file.write("<h4>"+speaker + "Variations </h4>" + '<br />')
        file.write('<table>')
    
        # TABLE HEADING
        file.write('<tr>')
        file.write('<th>Feature</th>')
        for ind, value in enumerate(variation_ids):
            file.write('<th> sent'+str(ind)+'</th>')
        file.write('</tr>')

        # WRITE ROWS
        for key in wav_filepath_dict:
            print('\n\n')
            print(wav_filepath_dict[key])
            print('\n\n')
            file.write('<tr>')
            file.write('<td>'+ key +'</td>')

            for fileid in wav_filepath_dict[key]:
                print('aaa', wav_filepath_dict[key][fileid])
                file_wavpath = wav_filepath_dict[key][fileid]
                file.write('<td> <audio controls=""><source src='+ file_wavpath + ' type="audio/wav"></audio> </td>')
                #Debug
                #file.write('<td>'+ file_wavpath +'</td>')

            file.write('</tr>')


        file.write('</table>')
        file.write('<br />')
        file.write('<hr />')
        file.write('<br />')


wav_directory = "testsamples_lj"

ctrl_values = ['-1.5', '-1.2','-1.0', '-0.8', '-0.6', '-0.4', '-0.2', '0', '0.2','0.5', '0.4', '0.6', '0.8', '1.0', '1.2', '1.5']
features = ['pa', 'pr', 'pd', 'se', 'st', 'f0std', 'all']

if __name__ == "__main__":
    outputfile = 'index.html'
    with open(outputfile, "w") as file:
        file.write("<html>\n")
        file.write(head_html)
        file.write("<body>\n")
        file.write("<h2>Model: FastSpeech2 Control</h2>" + '<br />')
    sentence_id_list =   ["LJ010-0252.wav","LJ021-0154.wav", "LJ046-0126.wav"]
    speaker = "LJ Speech"
    for sentence_id in sentence_id_list:
        wav_filepath_dict = arrange_table_cells(wav_directory, ctrl_values, sentence_id)
        generate_html_page(wav_filepath_dict, ctrl_values, speaker)

    # RYAN RYAN RYAN
    sentence_id_list =   ["sent01.wav","sent04.wav", "sent08.wav"]
    features = ['pa', 'pr', 'pd', 'se', 'st', 'f0std', 'all']
    wav_directory = "testsamples_ryan"
    speaker = "Ryan"
    for sentence_id in sentence_id_list:
        wav_filepath_dict = arrange_table_cells(wav_directory, ctrl_values, sentence_id)
        generate_html_page(wav_filepath_dict, ctrl_values, speaker)


    #Variation LJ
    sentence_id_list =   ["LJ010-0252.wav",  "LJ012-0250.wav",  "LJ018-0310.wav", "LJ021-0154.wav", "LJ032-0123.wav", "LJ046-0126.wav"]
    variation_ids = ['variationA', 'variationB', 'variationC', 'variationD', 'variationE']
    wav_directory = "lj_variation_result"
    speaker = "LJ Speech"
    table_cell_information = {}
    table_cell_information = {var_id: {} for var_id in variation_ids}
    for variation_id in variation_ids:
        for fn in os.listdir(os.path.join(wav_directory,variation_id)):
            fn_audio_path = os.path.join(wav_directory, variation_id, fn)
            table_cell_information[variation_id][fn] = fn_audio_path
    print(table_cell_information)
    generate_html_page_variation(table_cell_information, variation_ids,  speaker)


    
    #Variation Ryan
    sentence_id_list =   ["sent01.wav", "sent03.wav","sent04.wav", "sent08.wav", "sent09.wav", "sent10.wav"]
    variation_ids = ['variationA', 'variationB', 'variationC', 'variationD', 'variationE']  
    wav_directory = "ryan_variation_result"
    speaker = "Ryan"
    table_cell_information = {}
    table_cell_information = {var_id: {} for var_id in variation_ids}
    for variation_id in variation_ids:
        for fn in os.listdir(os.path.join(wav_directory,variation_id)):
            fn_audio_path = os.path.join(wav_directory, variation_id, fn)
            table_cell_information[variation_id][fn] = fn_audio_path
    print(table_cell_information)
    generate_html_page_variation(table_cell_information, variation_ids,  speaker)
    