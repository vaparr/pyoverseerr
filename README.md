[![PyPI version](https://badge.fury.io/py/pyoverseerr.svg)](https://badge.fury.io/py/pyoverseerr)
[![Downloads](https://pepy.tech/badge/pyoverseerr)](https://pepy.tech/project/pyoverseerr)

# pyoverseerr

This is a project for retrieving information from an Overseerr instance using their API.


# Installation

Run the following to install:
```python
pip install pyoverseerr
```


# Usage


#### Creating an object of your Overseerr instance

**Note:** You have to supply either a `password` or an `api_key` to successfully authenticate. The `api_key` will take precedence if both are supplied.

```python
import pyoverseerr

overseerr = pyoverseerr.Overseerr(
    ssl=True,
    host="192.168.1.120",
    port="5000",
    urlbase="overseerr/",
    username="MyUsername",
    password="MyPassword",
    api_key="pixf64thuh2m7kbwwgkqp52yznbj4oyo"
)
```

#### Authenticate

```python
overseerr.authenticate()
```

#### Testing connection to Overseerr

```python
try:
    overseerr.test_connection()
except pyoverseerr.OverseerrError as e:
    print(e)
    return
```

#### Retrieving data
```python
movies = overseerr.movie_requests
tv = overseerr.tv_requests
music = overseerr.music_requests

total = overseerr.total_requests
```

#### Searching

```python
movie_search = overseerr.search_movie("Movie Name")  
tv_search = overseerr.search_tv("TV show name")
music_search = overseerr.search_music_album("Album name")
```

#### Requesting
```python
overseerr.request_movie("theMovieDbId")
overseerr.request_tv("theTvDbId", request_latest=True)
overseerr.request_music("foreignAlbumId")
```

# License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
