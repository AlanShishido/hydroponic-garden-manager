class Pessoa(object):
    def _init_(
            self,
            name = str,
            address: str = None,
            current_location: str = None
    ):
        self.name: str = name
        self.address: str = address
        self.current_location: str = current_location

alan:Pessoa = Pessoa(name="string")

print(alan.name)