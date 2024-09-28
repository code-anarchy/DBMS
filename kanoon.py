import argparse
import logging
import http.client
import urllib.parse
import json

class IKApi:
    def __init__(self, token):
        self.logger = logging.getLogger('ikapi')
        self.headers = {'Authorization': 'Token %s' % token, 'Accept': 'application/json'}
        self.basehost = 'api.indiankanoon.org'
    
    def call_api(self, url):
        connection = http.client.HTTPSConnection(self.basehost)
        connection.request('POST', url, headers=self.headers)
        response = connection.getresponse()
        results = response.read()
        return results
    
    def search_cases(self, query, max_pages=1):
        """
        Search for cases based on a query string.

        :param query: The search query string.
        :param max_pages: The number of pages of results to retrieve.
        :return: List of cases found.
        """
        cases = []
        for pagenum in range(max_pages):
            encoded_query = urllib.parse.quote_plus(query.encode('utf8'))
            url = f'/search/?formInput={encoded_query}&pagenum={pagenum}&maxpages={max_pages}'
            response = self.call_api(url)
            obj = json.loads(response)
            
            if 'docs' not in obj:
                break
            
            for doc in obj['docs']:
                cases.append(doc)
        
        return cases

def initialize_ikapi_access(token):
    """
    Initializes access to the Indian Kanoon API using the provided token.

    :param token: API token for authentication.
    :return: An instance of the IKApi class.
    """
    if not token:
        raise ValueError("Token must not be empty.")

    # Set up logging (optional)
    logging.basicConfig(level=logging.INFO)

    # Create an instance of IKApi with the provided token
    ikapi_instance = IKApi(token)
    return ikapi_instance

# Example usage
if __name__ == "__main__":
    my_token = "77823e3b9b878ac55a92a93e75b317220f9cc85c"  # Replace with your actual token
    ikapi = initialize_ikapi_access(my_token)

    # Define your search query here
    query = "Civil Law"  # Example query
    max_pages = 1  # Specify how many pages of results you want

    try:
        cases = ikapi.search_cases(query=query, max_pages=max_pages)
        print(f"Found {len(cases)} cases:")
        if cases:
            case = cases[0]
            print(f"Title: {case['title']}, Court: {case['docsource']}, Date: {case['publishdate']}")
    except Exception as e:
        print(f"An error occurred: {e}")
