#importing kaggle
import kaggle 
from zipfile36 import ZipFile

#importing kaggleAPI 
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
#authenticating kaggleApi
api.authenticate()

#list of  all available dataset
api.dataset_list()
#searching for the required dataset from all available dataset using keyword
api.dataset_list(search='drone')
#downloading the required dataset as zipfile
api.dataset_download_files("dasmehdixtr/drone-dataset-uav")
#storing the zipfile in preferred location
zf = ZipFile('drone-dataset-uav.zip')
zf.extractall('C:\\Users\\Chandana\\Desktop\\droneDATA\\')
zf.close()
