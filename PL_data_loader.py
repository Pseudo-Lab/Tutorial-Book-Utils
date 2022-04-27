# taken from this repo: https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url

import gdown
import argparse

file_destinations = {'FaceMaskDetection':'Face Mask Detection.zip',
              'COVIDTimeSeries':'COVIDTimeSeries.zip',
              'GAN-Colorization':'Victorian400-GAN-colorization-data.zip',
              'NLP-QG':'CoNLL+BEA_corrected_essays.pkl'}

file_id_dic = {'FaceMaskDetection':'1pJtohTc9NGNRzHj5IsySR39JIRPfkgD3',
              'COVIDTimeSeries':'1B36Djko-f0LtVxSaBEVYosLTTsu0qtsh',
              'GAN-Colorization':'1tPNnwPISjPaC1nDZ1QpXcJAQCFmeO3Uv',
              'NLP-QG':'1dPa5iLEv6WqeHZaYhNLPw5q_i5IGJzU9'}

def download_file_from_google_drive(id_, destination):
    url = f'https://drive.google.com/uc?id={id_}'
    output = destination
    gdown.download(url, output, quiet=False)
    print(f'{output} download complete!')
    
parser = argparse.ArgumentParser(description = 'data loader for PseudoLab Tutorial Book')

parser.add_argument('--data', type = str, help = 'key for selecting data')

args = parser.parse_args()

download_file_from_google_drive(id_=file_id_dic[args.data], destination=file_destinations[args.data])
