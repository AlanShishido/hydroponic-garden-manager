class Pessoa(object):
    def _init_(
            self,
            name: str = None,
            address: str = None,
            current_location: str = None
    ):
        self.name: str = name
        self.address: str = address
        self.current_location: str = current_location

    def walk_to(self, destiny: str):
        self.current_location = destiny


class Funcionario(Pessoa):
    def _init_(
            self,
            matricula: str,
            name: str = None,
            address: str = None
    ):
        super(Funcionario, self)._init_(
            name=name,
            address=address
        )
        self.matricula: str = matricula


luiz: Funcionario = Funcionario(
    name='luiz',
    address='address #1',
    matricula='#1033143'
)
print(luiz.name)
print(luiz.matricula)
print(luiz.current_location)
luiz.walk_to('fpf')
print(luiz.current_location)

cassio: Pessoa = Pessoa(
    name='cassio',
    address='home',
    current_location='home'
)
print(cassio.name)
print(cassio.current_location)