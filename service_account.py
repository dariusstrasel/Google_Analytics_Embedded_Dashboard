"""service-account.py
Gets an access token for the Google Analytics Embed API.
"""

from oauth2client.service_account import ServiceAccountCredentials
from s3_arbitrator import getJSONKeyDictionary

# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'



def get_access_token():
    """Returns an OAuth access token  """
    try:
        jsonKeyDict = getJSONKeyDictionary()
        return str(ServiceAccountCredentials.from_json_keyfile_dict(
             jsonKeyDict, SCOPE).get_access_token().access_token)

    except Exception as error:
        print("Authorization to Google Analytics dashboard failed; check Oauth token or auth flow on google developer console.")
        return None



if __name__ == "__main__":
    print(get_access_token())
