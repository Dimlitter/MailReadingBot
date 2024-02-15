import asyncio
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient

from kiota_abstractions.api_error import APIError

credential = ClientSecretCredential(
    'tenant_id',
    'client_id',
    'client_secret'
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credentials=credential, scopes=scopes)
# Get the user

async def get_user():
    try:
        user = await client.users.by_user_id('userID').get()
        print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')
asyncio.run(get_user())


