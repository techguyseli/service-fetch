# service-fetch

## Description

This is a python project that scraps basic service data and image urls in a given map area, utilizing [rapidapi's travel-advisor api](https://rapidapi.com/apidojo/api/travel-advisor).

## Steps

1) Clone the project

```bash
git clone https://github.com/techguyseli/service-fetch
```

2) Change the directory to service-fetch/service-fetch

```bash
cd service-fetch/service-fetch
```

3) Run this script for help/usage

```bash
python3 servicefetch.py -h
```

You should see something like this

```bash
Usage:
        python3 servicefetch.py --option1 value1 --option2 value2. . .

Mandatory options:
        --apikey value : A RapidApi travel-advisor api key.
        --nelat value : Latitude of north east point of the border box.
        --nelon value : Longitude of north east point of the border box.
        --swlat value : Latitude of south west point of the border box.
        --swlon value : Longitude of south west point of the border box.

Optional options:
        --srvfile value : Name of the file to store info about the images.
        --imgfile value : Name of the file to store info about the services.
        --help or -h : Print this help menu.
```

## Basic usage

For linux:

```bash
python3 servicefetch.py --apikey abcdefghijklmnopqrstuvwxyz1234 --nelat 34.015615 --nelon -6.837911 --swlat 34.027139 --swlon -6.817054
```

For windows:

```bash
py servicefetch.py --apikey abcdefghijklmnopqrstuvwxyz1234 --nelat 34.015615 --nelon -6.837911 --swlat 34.027139 --swlon -6.817054
```

## Note

You can get the coordinates of the north east and south west points from [google maps](https://www.google.com/maps) or any geolocation/mapping service.

The north east point is the upper right corner of the map area you want to process.

And the south west point is the lower left corner of the same map area.

