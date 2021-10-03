import boto3

# Cria o serviço com as credenciais da AWS
s3 = boto3.client(
    service_name='s3', region_name='us-east-1', aws_access_key_id='access_key', aws_secret_access_key='secret_key'
)

# Sobe o arquivo para o local desejado no s3

s3.upload_file(r'pycode.jpg', 'bucket', 'pycode.jpg')
