# Variable constant to project

class DatabaseInfo(object):
    # * Nome da base principal 
    DIRECTORY = 'database/data'
    TABLE_NAME = 'hidroponia_automatica.db'

    SOURCE = DIRECTORY + '/' + TABLE_NAME

    # Armazenamento de alguns dados por exemplo:
    #   Valor de PH
    #   Valor de Condutividade (TDS)
    #   Valor de Temperatura Ambiente
    #   Valor de Temperatura da Água
    #   Valor de Corrente utilizada

'''
Number  51xx to codig information comunication interprocess
'''

class INFO(object):
    INFO_TESTING_CLASS = 5100
    
    pass