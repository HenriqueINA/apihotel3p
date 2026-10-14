from flask_restful import Resource

lista_hoteis = [
    { "hotel_id" : "Rojao", "nome": "Tasca do Fred", "estrelas": 67, "diaria": 123, "cidade": "Ribeirao" },
    { "hotel_id" : "Francesinha", "nome": "Samu", "estrelas": 76, "diaria": 321, "cidade": "Sao Martinho" },
    { "hotel_id" : "Infantario", "nome": "Granja", "estrelas": 1, "diaria": 000, "cidade": "Fama" }
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": lista_hoteis }