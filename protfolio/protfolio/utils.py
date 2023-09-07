# utils.py

import httpx

from django.conf import settings

def upload_file_to_supabase(file, file_name):
    api_url = settings.SUPABASE_API_URL
    api_key = settings.SUPABASE_API_KEY

    with httpx.Client() as client:
        response = client.post(
            f'{api_url}/storage/v1/upload/public/{file_name}',
            headers={'apikey': api_key},
            files={'file': (file_name, file)}
        )

    if response.status_code == 200:
        return f'{api_url}/storage/v1/public/{file_name}'
    else:
        raise Exception(f'Failed to upload file to Supabase: {response.status_code}')
