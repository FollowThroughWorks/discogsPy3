import oauth1forpy3
import discogsObject
import json


class Client(oauth1forpy3.Client):
    request_url = r"https://api.discogs.com/oauth/request_token"
    access_url = r"https://api.discogs.com/oauth/access_token"
    verification_url = r"http://discogs.com/oauth/authorize?oauth_token="
    base_url = r"https://api.discogs.com/"

    def __init__(self,user_agent,key='',secret='',callback=''):
        oauth1forpy3.Client.__init__(self,key,secret,user_agent,Client.request_url,Client.access_url,Client.verification_url)

    def release_by_id(self,id):
        return discogsObject.Release(self.retrieve_page(self.base_url + r"/releases/" + str(id)),self)

    def master_by_id(self,id):
        return discogsObject.Master(self.retrieve_page(self.base_url + r"/masters/" + str(id)),self)

    def artist_by_id(self,id):
        return discogsObject.Artist(self.retrieve_page(self.base_url + r"/artists/" + str(id)),self)

    def artist_by_name(self,name):
        new_name = str.replace(name," ","+")
        search_result = self.retrieve_page(self.base_url + r"/database/search?q=" + new_name + r"&type=artist")
        try:
            first_result = json.loads(search_result)['results'][0]['id']
            return self.artist_by_id(first_result)
        except(IndexError):
            print("No result found")
            return None

    def label_by_id(self,id):
        return discogsObject.Label(self.retrieve_page(self.base_url + r"/labels/" + str(id)),self)

    def search(self,query,search_type=""):
        new_name = str.replace(query," ","+")
        search_results = self.retrieve_page(self.base_url + r"/database/search?q=" + new_name + r"&type=" + search_type)
        try:
            results = json.loads(search_results)['results']
            return results
        except(IndexError):
            print("No result found")
            return None
