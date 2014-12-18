__author__ = 'Mike'
import json
import discogsPy3
import time

class DiscogsObject():
    def __init__(self,page):
        self.data = json.loads(page)
        for item in self.data:
            self.createProperty(item)
    def createProperty(self,keyToGet):
        setattr(self,keyToGet,self.data[keyToGet])

class Artist(DiscogsObject):
    def __init__(self,page,client):
        DiscogsObject.__init__(self,page)
        self.client = client

    def releases(self):
        final_releases = []
        release_page = self.client.retrieve_page(self.resource_url + "/releases")
        releases = json.loads(release_page)
        for item in releases['releases']:
            try:
                new_release =  self.client.release_by_id(item['main_release'])
                final_releases.append(new_release)
                time.sleep(1)
            except:
                pass
        return final_releases

    def group_list(self):
        final_groups = []
        for item in self.groups:
            try:
                new_group = self.client.artist_by_id(item['id'])
                final_groups.append(new_group)
                time.sleep(1)
            except:
                pass
        return final_groups

    def member_list(self):
        final_members = []
        for item in self.members:
            try:
                new_member = self.client.artist_by_id(item['id'])
                final_members.append(new_member)
                time.sleep(1)
            except:
                pass
        return final_members


class Master(DiscogsObject):
    def __init__(self,page,client):
        DiscogsObject.__init__(self,page)
        self.client = client

    def artist_list(self):
        final_artists = []
        for item in self.artists:
            try:
                new_artist = self.client.artist_by_id(item['id'])
                final_artists.append(new_artist)
                time.sleep(1)
            except:
                pass
        return final_artists

    def artist(self):
        final_artists = []
        this_artist = self.client.artist_by_id(self.artists[0]['id'])
        return this_artist

class Release(DiscogsObject):
    def __init__(self,page,client):
        DiscogsObject.__init__(self,page)
        self.client = client

    def artist_list(self):
        final_artists = []
        for item in self.artists:
            try:
                new_artist = self.client.artist_by_id(item['id'])
                final_artists.append(new_artist)
                time.sleep(1)
            except:
                pass
        return final_artists

    def artist(self):
        final_artists = []
        this_artist = self.client.artist_by_id(self.artists[0]['id'])
        return this_artist

    def label_list(self):
        final_labels = []
        for item in self.labels:
            try:
                new_label = self.client.label_by_id(item['id'])
                final_labels.append(new_label)
                time.sleep(1)
            except:
                pass
        return final_labels

class Label(DiscogsObject):
    def __init__(self,page,client):
        DiscogsObject.__init__(self,page)
        self.client = client

    def releases(self,pages=1):
        final_releases = []

        release_page = self.client.retrieve_page(self.resource_url + "/releases")
        releases = json.loads(release_page)
        max_pages = releases['pagination']['pages']
        if pages > max_pages:
            pages = max_pages

        for x in range(0,pages):
            release_page = self.client.retrieve_page(self.resource_url + "/releases?page=" + str(x))
            releases = json.loads(release_page)
            for item in releases['releases']:
                try:
                    new_release =  self.client.release_by_id(item['id'])
                    final_releases.append(new_release)
                    time.sleep(1)
                except:
                    pass
        return final_releases
