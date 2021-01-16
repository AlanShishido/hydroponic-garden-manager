import peewee
from datetime import date, datetime
from choices import DBConstant as db

project_db = peewee.SqliteDatabase(db.SOURCE)

class BaseModel(peewee.Model):

    class Meta:
        database = project_db

class LettuceDatas(BaseModel):
    acquired_date = peewee.DateField()
    acquired_time = peewee.TimeField()
    ph = peewee.FloatField()
    tds = peewee.FloatField()
    ambient_temp = peewee.FloatField()
    water_temp = peewee.FloatField()
    
class Gardens(BaseModel):
    name = peewee.CharField()
    number = peewee.IntegerField()
    datas = peewee.ForeignKeyField(LettuceDatas)

class DatabaseBase(object):
    pass

class DBManager(DatabaseBase):

    def save_new_data(self,
                      garden_name=str,
                      data=str
                      ):

        print("armazenando dados")

        # * Exemplo de armazenamento de dados
        # Armazena no banco de dados e atribui na variavel o id
        lettuce_0 = LettuceDatas.create(
            acquired_date=date.today(),
            acquired_time=datetime.now(),
            ph=1.5234,
            tds=123.123,
            ambient_temp=32,
            water_temp=24
        )
        Gardens.create(
            name=garden_name,
            number=0,
            datas=lettuce_0
        )

    def consult_data(self):
        # TODO verificar a parte de leitura de dados
        print('consultando dados')


if __name__ == "__main__":
    test = DBManager()
    test.save_new_data("jardin 1", "instancia")


# try:
#     Gardens.create_table()
#     print("Tabela 'Horta' criada com sucesso!")
# except peewee.OperationalError:
#     print("Tabela 'Horta' ja existe!")

# try:
#     LettuceDatas.create_table()
#     print("Tabela 'Dados da Alface' criada com sucesso!")
# except peewee.OperationalError:
#     print("Tabela 'Dados da Alface' ja existe!")

