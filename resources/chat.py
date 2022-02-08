# API nin yanıt verdiği, düşündüğü dosyalar resource klasörü altında yer almaktadır. 

from flask_restful import Resource, reqparse


class Chat(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('msg',
        type = str,
        required = True,
        help = "Mesaj alani bos birakilamaz!")

    def post(self):
        data = Chat.parser.parse_args()
        print(f"Girdi: {data['msg']}")
        result = {"cevap": f'Sorgunun body değeri: {data["msg"]}'}
        print(result)
        return result

