# FIT to Heatmap Overview

Majority of my ride files these days are in FIT format. I needed a way to parse FIT files and generate heatmap

Python code to parse FIT files and create heatmap:
* Use fitdecode to parse FIT files and get all the coordinates
* Pass all the coordinates into Google Maps to create heatmap
* You will need your own Google Maps API in the config.ini for the maps to render



## Usage

**Install Dependencies**

```bash
$ python3 -m pip install -r requirements.txt
```

#### Command:

Show help:
```bash
$ python3 heatmap.py --help
Usage: heatmap.py [OPTIONS]

Options:
  --output TEXT                   Specify the name of the output file.
                                  Defaults to `map`
  --input TEXT                    Specify an input folder. Defaults to `fit`
  --filter [running|cycling|walking]
                                  Specify a filter type. Defaults to no filter
  --help                          Show this message and exit.
  --year                          Specify a year. Defaults to no year. Multiple years can be accepted
```

Examples:
```bash
$ python3 heatmap.py
$ python3 heatmap.py --input fit --output map
$ python3 heatmap.py --input fit --output map2 --year 2019
$ python3 heatmap.py --input fit --output map3 --year 2019 --year 2020
```

#### Retrieving FIT Files

- Strava users can follow [Strava's instructions](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export) to export FIT data

#### Inspiration
- This is inspired by https://github.com/TomCasavant/GPXtoHeatmap

