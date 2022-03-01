# FIT to Heatmap Overview
Python code to parse FIT files and create heatmap

This is inspired by https://github.com/TomCasavant/GPXtoHeatmap



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

#### Retrieving GPX Files

- Strava users can follow [Strava's instructions](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export) to export FIT data


