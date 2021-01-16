# Variable constant to project

'''
Number  51xx to codig information comunication interprocess
'''

class ModelBase(object):
    pass

class InfoConstant(ModelBase):
    INFO_TESTING_CLASS = 5100
    

class DBConstant(ModelBase):
    
    # * Nome da base principal 
    DIRECTORY = 'src/data'
    TABLE_NAME = 'hidroponia_automatica.db'

    SOURCE = DIRECTORY + '/' + TABLE_NAME

    # Armazenamento de alguns dados por exemplo:
    #   Valor de PH
    #   Valor de Condutividade (TDS)
    #   Valor de Temperatura Ambiente
    #   Valor de Temperatura da Água
    #   Valor de Corrente utilizada

class ViewConstant(ModelBase):
    
    # * Cores da View
    BG_GREEN = '#65aa34'
    AERO_BLUE = '#D7FDF0'
    MAGIC_MINT_1 = '#B2FFD6'
    MAGIC_MINT_2 = '#B3EBD5'
    OPAL = '#B4D6D3'
    LAVENDER_GRAY = '#B8BAC8'
    AFRICAN_VIOLET = '#AA78A6'