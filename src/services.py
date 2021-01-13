from datetime import date, datetime
from database_models import Gardens, LettuceDatas


class DBManager(object):
    
    def save_new_data(self,
        garden_name = str,
        data = str
        ):

        print("passei por aqui")

        # * Exemplo de armazenamento de dados
        # Armazena no banco de dados e atribui na variavel o id 
        lettuce_0 = LettuceDatas.create(
            acquired_date= date.today(),
            acquired_time= datetime.now(),
            ph= 1.5234,
            tds= 123.123,
            ambient_temp= 32,
            water_temp=24
            )
        Gardens.create(
            name=garden_name,
            number=0,
            datas= lettuce_0
        )

    def consult_data(self):
        # TODO verificar a parte de leitura de dados
        pass    


if __name__ == "__main__":
    test = DBManager()
    test.save_new_data("jardin 1", "instancia")