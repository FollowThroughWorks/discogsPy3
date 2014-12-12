discogsPy3
==========

Library for using the discogs API with Python 
requires oauth1forpy3 

### Creating the authenticated connection to discogs:
  1. Create an instance of the Client object. You must have:
      * a consumer key and secret, received from the site you're accessing
      * a user agent
  2. 
     1. If you already have an access key and secret:
      * Client.set_access_token(your key,your secret)
     2. Else 
      * call Client.set_access_token() and it will use the consumer key and secret to acquire them
      * (if you want to then get the access token and secret for further use, call .access_token and .access_token_secret)

# Accessing discogs info
There are objects for:
* Artists
* Releases
* Master Releases
```
d = discogsPy3.Client(consumer_key,consumer_secret,user_agent)
d.set_access_token()
```
To get an artist by their site id:
`fot = d.artist_by_id(381567)`

To get an artist by their name
`thrice = d.artist_by_name('thrice')`

Once you have an artist, you can access their information like normal attributes:
```
>>> thrice.name
'Thrice'
>>> thrice.id
261347
>>> thrice.profile
'American rock band from Irvine, California, formed in 1998. Following their spring 2012 tour, the band went on hiatus.'
```
