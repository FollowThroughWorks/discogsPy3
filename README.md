discogsPy3
==========

Library for using the discogs API with Python 
requires oauth1forpy3 

### Creating the (optionally authenticated) connection to discogs:
  1. Create an instance of the Client object:
      * You must have a user agent, preferably following [RFC 1945](http://tools.ietf.org/html/rfc1945#section-3.7)
      * If you are searching or using user information you must also included the consumer key and secret
```
d = discogsPy3.Client(user_agent,consumer_key,consumer_secret) # Consumer key and secret are optional
```
  2. 
     1. If you already have an access key and secret:
      * Client.set_access_token(your key,your secret)
     2. Else 
      * call Client.set_access_token() and it will use the consumer key and secret to acquire them
      * (if you want to then get the access token and secret for further use, call .access_token and .access_token_secret)
```
>>d.set_access_token() 
>>d.access_token
your access token
>>d.access_token_secret
your access token secret
```
### Accessing discogs info
There are objects for:
* Artists
* Releases
* Master Releases
* 
#### Artists
To get an artist by their site id:
```
fot = d.artist_by_id(381567)`
```
To get an artist by their name:
```
dep = d.artist_by_name("the dillinger escape plan")
```

Once you have an artist, you can access their information like normal attributes:
```
>>> thrice.name
'Thrice'
>>> thrice.id
261347
>>> thrice.profile
'American rock band from Irvine, California, formed in 1998. Following their spring 2012 tour, the band went on hiatus.'
```
To retrieve their releases, as Release objects, call the releases() method:
```
>>> tsosis_releases = tsosis.releases()
>>> for release in tsosis_releases:
	print(str(release.year) + " - " + release.title)
	
2009 - Blue Version
2010 - Red Version
```
To retrieve their members, as Artist objects, call the member_list() method:
```
[member.name for member in destinys_child.member_list()]
['Beyoncé Knowles', 'Farrah Franklin', 'Kelly Rowland', 'Latavia Roberson', 'Letoya Luckett', 'Michelle Williams']
```
To retrieve groups they've performed in, as Artist objects, call the group_list() method:
```
[group.name for group in chris_pennie.group_list()]
['Coheed And Cambria', 'Dillinger Escape Plan, The']
```

A list of Artist properties and methods:
* **name** - the artist's/band's name
* **profile** - a description of the artist
* **urls** - a list of the artist's web pages
* **members** - a list comprised of a dictionary of info for each member
* **member_list()** - a list of Artist objects for each member
* **groups** - a list comprised of a dictionary of info for each group the artist has performed with
* **member_list()** - a list of Artist objects for each group the artist has performed with
* **namevariations** - variations of the artist's name
* **images** - a list comprised of a dictionary of info for each image associated with the artist
* **data** - A dictionary of the information provided by discogs.com
* **resource_url** - where the discogs.com info can be found

#### Releases
Works similarly to artists:
To get by site id:
`fot = d.release_by_id(381567)`

Once you have a release, you can access its information like normal attributes:
```
>>> CLPPNG.title
'CLPPNG'
>>> CLPPNG.year
2014
>>> CLPPNG.genres
['Electronic', 'Hip Hop']
```

To retrieve the artist, as an Artist object, call the artist() method:
```
>>> clipping = CLPPNG.artist()
>>> clipping.name
'Clipping.'
```

To retrieve a list of artists as Artist objects (in case multiple worked on a release), call artist_list() instead:
```
>>> cfop_artists = cfop.artist_list()
>>> for artist in cfop_artists:
	print(artist.name)

By The End Of Tonight
Tera Melos
```
