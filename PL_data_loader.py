# taken from this repo: https://github.com/nsadawi/Download-Large-File-From-Google-Drive-Using-Python/
import requests
import os
import os.path as pth
# from multiprocessing import Pool
# from functools import partial
# from tqdm.notebook import tqdm
import zipfile
import argparse

def download_file_from_google_drive(id_, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params = { 'id' : id_ }, stream = True)
    token = get_confirm_token(response)
    if token:
        params = { 'id' : id_, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)
        
    basename = response.headers['Content-Disposition'].split(';')[1].split('filename=')[1].replace('\"', '')
    full_dst_filenname = pth.join(destination, basename)
    save_response_content(response, full_dst_filenname)
    return full_dst_filenname

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

file_id_list = [
    '1pJtohTc9NGNRzHj5IsySR39JIRPfkgD3', #Pseudo Lab Drive
]

file_id_dic = {'FaceMaskDetection':'1pJtohTc9NGNRzHj5IsySR39JIRPfkgD3',
              'COVIDTimeSeries':'1B36Djko-f0LtVxSaBEVYosLTTsu0qtsh',
              'GAN-Colorization':'1tPNnwPISjPaC1nDZ1QpXcJAQCFmeO3Uv'}

destination = '' ### YOUR_DOWNLOAD_PATH
# os.makedirs(destination, exist_ok=True)

filename_list = []



parser = argparse.ArgumentParser(description = 'data loader for PseudoLab Tutorial Book')

parser.add_argument('--data', type = str, help = 'key for selecting data')

args = parser.parse_args()


filename = download_file_from_google_drive(id_=file_id_dic[args.data], destination=destination)
print('{} is done!'.format(filename))
filename_list.append(filename)

# ### Use single process
# for file_id in file_id_list:
#     filename = download_file_from_google_drive(id_=file_id, destination=destination)
#     print('{} is done!'.format(filename))
#     filename_list.append(filename)

### If you want to download more faster
# download_func = partial(download_file_from_google_drive, destination=destination)
# with Pool(4) as pool:
#     for i, filename in tqdm(enumerate(pool.imap_unordered(download_func, file_id_list)), total=len(file_id_list)):
#         print('{} is done!'.format(filename))
#         filename_list.append(filename)
