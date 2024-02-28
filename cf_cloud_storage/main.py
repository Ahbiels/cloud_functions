import json

def hello_gcs(event):
    data = event.data

    print('-----------------------------//------------------------------')
    print(f"Dados: {data}")
    print(f"Evento: {event}")

    data_str = data.decode('utf-8')

    # Converter a string para um dicionário
    data_dict = json.loads(data_str)

    # Extrair o ID e o nome da bucket
    object_id = data_dict['id']
    object_name = data_dict['name']
    object_type = data_dict['contentType']
    object_updated = data_dict['updated']
    bucket_name = data_dict['bucket']
    bucket_storage = data_dict['storageClass']

    print(f"ID do objeto: {object_id}")
    print(f"Nome do objeto: {object_name}")
    print(f"Tipo do objeto: {object_type}")
    print(f"Atualização do objeto: {object_updated}")
    print(f"Nome da Bucket: {bucket_name}")
    print(f"Classe de armazenamento: {bucket_storage}")