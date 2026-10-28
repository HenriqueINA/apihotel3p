from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required

# lista_hoteis = [
#     { "hotel_id" : "Rojao", "nome": "Tasca do Fred", "estrelas": 5, "diaria": 123, "cidade": "Ribeirao" },
#     { "hotel_id" : "Francesinha", "nome": "Samu", "estrelas": 4.6, "diaria": 321, "cidade": "Sao Martinho" },
#     { "hotel_id" : "Infantario", "nome": "Granja", "estrelas": 2, "diaria": 000, "cidade": "Fama" }
# ]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": [hotel.json() for hotel in HotelModel.query.all()] }

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=True, help="Nome obrigatório")
    argumentos.add_argument("estrelas", type=float, required=True, help="Estrelas obrigatório")
    argumentos.add_argument("diaria", type=float, required=True, help="Diária obrigatório")
    argumentos.add_argument("cidade", type=str, required=True, help="Cidade obrigatório")

    def get(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            return hotel.json(), 200
        return { "message": "Hotel not found" }, 404

    @jwt_required()
    def post(self,id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionário
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            return { "message": "Hotel with this id already exists" }
        try:
            novo_hotel = HotelModel(id_hotel, **dados)
            novo_hotel.save_hotel()
            return novo_hotel.json(), 200
        except:
            return { "message": "Internal error ..." }, 500 # Internal error
    
    @jwt_required()
    def put(self, id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionário
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel["hotel_id"] == id_hotel:
            try:
                hotel.update_hotel(dados["nome"], dados["estrelas"], dados["diaria"], dados["cidade"])
                hotel.save_hotel()
                return hotel.json(), 200
            except:
                return { "message": "Internal error ..." }, 500 # Internal error
        try:
            novo_hotel = HotelModel(id_hotel, **dados)
            novo_hotel.save_hotel()
            return novo_hotel.json(), 201 # Created
        except:
            return { "message": "Internal error ..." }, 500 # Internal nigger
        
    @jwt_required()
    def delete(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            try:
                hotel.delete.hotel()
                return { "message": "Hotel deleted" }, 200
            except:
                return { "message": "Internal error ..." }, 500 # Internal error
        return { "message": "Hotel not found" }, 404
            