from flask_restful import Resource, reqparse

lista_hoteis = [
    { "hotel_id" : "Rojao", "nome": "Tasca do Fred", "estrelas": 5, "diaria": 123, "cidade": "Ribeirao" },
    { "hotel_id" : "Francesinha", "nome": "Samu", "estrelas": 4.6, "diaria": 321, "cidade": "Sao Martinho" },
    { "hotel_id" : "Infantario", "nome": "Granja", "estrelas": 2, "diaria": 000, "cidade": "Fama" }
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": lista_hoteis }

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=True, help="Nome obrigatório")
    argumentos.add_argument("estrelas", type=float, required=True, help="Estrelas obrigatório")
    argumentos.add_argument("diaria", type=float, required=True, help="Diária obrigatório")
    argumentos.add_argument("cidade", type=str, required=True, help="Cidade obrigatório")

    def get(self, id_hotel):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel, 200
            return { "message": "Hotel not found" }
        
    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionário
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return { "message": "Hotel with this id already exists" }
        novo_hotel = { "hotel_id": id_hotel, **dados}
        lista_hoteis.append(novo_hotel)
        return hotel, 200
    
    def put(self, id_hotel):
        ...
    def delete(self, id_hotel):
        ...