import kaggle 
from zipfile36 import ZipFile

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

api.dataset_list()

api.dataset_list(search='drone')

api.dataset_download_files("dasmehdixtr/drone-dataset-uav")

zf = ZipFile('drone-dataset-uav.zip')
zf.extractall('C:\\Users\\Chandana\\Desktop\\droneDATA\\')
zf.close()
