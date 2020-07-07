############################################################################################
################################ Descripcion################################################
__author__ = "Jorge Cardona"
__copyright__ = "Copyright 2020, MACHINE LEARNING PROJECT"
__credits__ = "Jorge Cardona"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Jorge cardona "
__email__ = "https://github.com/JorgeCardona"
__status__ = "Production"
###############################################################################################
###############################################################################################

import os
import pathlib
import logging

# lee la ruta del directorio del proyecto
ROOT_DIRECTORY = str(os.getcwd()).replace('\\','/')

# asigna los directorios para acceder a los recursos de la API
RESOURCES_DIRECTORY      = ROOT_DIRECTORY      + '/RESOURCES'
LOG_FILE_NAME            = 'logging.log'
LOG_FOLDER               = RESOURCES_DIRECTORY + '/LOG'
LOG_DIRECTORY            = LOG_FOLDER          + '/' + LOG_FILE_NAME
UPLOAD_FILES_DIRECTORY   = RESOURCES_DIRECTORY + '/FILES'
FILE_LOCATION_LABEL      = 'FILE_LOCATION'
CONFIGURATION_DIRECTORY  = RESOURCES_DIRECTORY + '/CONFIGURATION'
TRAINED_MODELS_DIRECTORY = RESOURCES_DIRECTORY + '/TRAINED_MACHINE_LEARNING_MODELS'
MAIN_DIRECTORIES         = [LOG_FOLDER, UPLOAD_FILES_DIRECTORY, TRAINED_MODELS_DIRECTORY]

# configuraciones flash 
logging.basicConfig(filename=LOG_DIRECTORY, level=logging.INFO)
FLASK_PORT = 5000
FLASK_DEBUG = True

# archivos soportados y tamano maximo permitido
MAX_CONTENT_LENGTH      = 16 * 1024 * 1024
ALLOWED_SAVE_SERVICES   = ['SUPERVISED','NLP','COMPUTER_VISION','TEXT_ANALYTICS']
ALLOWED_EXTENTION_FILES = set(['CSV','XLS','XLSX'])

# credenciales de la base de datos
#MONGODB
MONGODB_HOST                  = 'localhost'
MONGODB_PORT                  = '27017'
MONGODB_USER                  = ''
MONGODB_PASS                  = ''
MONGODB_DATABASE_NAME         = 'db'
MONGODB_URL_CONNECTION        = 'mongodb://' + MONGODB_HOST +':' + MONGODB_PORT +'/'


# MYSQL
MYSQL_CHARSET               = '?charset=utf8mb4&binary_prefix=true'
MYSQL_HOST                  = 'localhost'
MYSQL_PORT                  = '3306'
MYSQL_USER                  = 'root'
MYSQL_PASS                  = ''
MYSQL_DATABASE_NAME         = 'db'
MYSQL_URL_CONNECTION        = 'mysql+pymysql://' + MYSQL_USER + ':' + MYSQL_PASS  + '@' +  MYSQL_HOST + ':' + MYSQL_PORT +'/' + MYSQL_DATABASE_NAME + MYSQL_CHARSET


# database types
DATA_BASES_TYPES = ['MONGODB','MYSQL']

# dataframe
NA_REPLACE_SYMBOL = '^-^'
NA_RECOVERY_VALUE = ''
ID_FOR_DATA_SAVE  = 'ID'


# Tablas y colecciones para persistencia
ALL_DATA     = 'clima'
PREDICTION   = 'datos_prediccion'
CLASIFICATOR = 'mejor_clasificador'

# tratamiento de data para entrenamiento

TRAINING_PORCENTAGE = 0.3
BINARIZATION_LIMIT  = 24.5
TARGET_COLUMN       = ''
BINARIZATED_TARGET_COLUMN = ''