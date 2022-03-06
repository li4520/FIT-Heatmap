import click
from configparser import ConfigParser
import fitdecode
import os
# from datetime import datetime

parser = ConfigParser()
parser.read('config.ini')
API_KEY = parser.get('GOOGLE', 'API_KEY')
INITIAL_LATITUDE = parser.get('MAP', 'LATITUDE')
INITIAL_LONGITUDE = parser.get('MAP', 'LONGITUDE')
INITIAL_ZOOM = parser.get('MAP', 'ZOOM')


@click.command()
@click.option("--output", default="map", help="Specify the name of the output file. Defaults to `map`")
@click.option("--input", default="fit", help="Specify an input folder. Defaults to `fit`")
@click.option("--filter", default=None, help="Specify a filter type. Defaults to no filter", type=click.Choice(['running', 'cycling', 'walking']))
@click.option("--year", default=None, help="Specify a year. Defaults to no year", type=int, multiple=True)

def main(output, input, filter, year):
    points = load_points(input, filter, year)
    generate_html(points, output)


# Convert Garmin time format to Python datetime - not needed anymore.
""" 
def convert_frame_datetime(frame_datetime):
    converted_frame_datetime = datetime.strptime(
        frame_datetime, "%Y-%m-%d %H:%M:%S%z")

    return converted_frame_datetime 
"""


# Get fit file's created time
def get_fit_time(input_file):
    with fitdecode.FitReader(input_file) as fit_file:
        for frame in fit_file:
            if isinstance(frame, fitdecode.records.FitDataMessage):
                if frame.name == 'file_id':
                    if frame.has_field('time_created'):
                        # print(frame.get_value('time_created').year)
                        x = frame.get_value('time_created')
                        return x


def load_points(folder, filter, year):
    # Loads all fit files into a list of points
    coords = []

    # Loads files with progressbar
    print(f"Loading files with type {filter} for {year}...")
    with click.progressbar(os.listdir(folder)) as bar:
        for filename in bar:
            # Verify file is a fit file
            if (filename.lower().endswith(".fit")):
                fit_file = os.path.join(folder, filename)
                # Get fit file's created date
                fit_created_year = get_fit_time(fit_file).year
                # Only continue if year list is empty OR fit file's year is part of the year(s) you want to process
                if not year or fit_created_year in year:
                    with fitdecode.FitReader(fit_file) as fit:
                        for frame in fit:
                            if isinstance(frame, fitdecode.records.FitDataMessage):
                                # only pull 'record' frame - this is where coordinates are
                                if frame.name == 'record':
                                    if frame.has_field('position_lat') and frame.has_field('position_long'):
                                        # Get Garmin Lat and Long from each frame
                                        # Convert Garmin GPS coordinates, calculcations based on this https://gis.stackexchange.com/questions/122186/convert-garmin-or-iphone-weird-gps-coordinates/368905#368905
                                        frame_lat = float(frame.get_value(
                                            'position_lat')) / ((2**32)/360)
                                        frame_long = float(frame.get_value(
                                            'position_long')) / ((2**32)/360)
                                        coords.append(
                                            [frame_lat, frame_long])

    return (coords)


def get_outline():
    """Reads in the html outline file"""
    with open('map-outline.txt', 'r') as file:
        outline = file.read()
    return outline


def generate_html(points, file_out):
    """Generates a new html file with points"""
    if not os.path.exists('output'):
        os.mkdir('output')
    f = open(f"output/{file_out}.html", "w")
    outline = get_outline()
    google_points = ",\n".join(
        [f"new google.maps.LatLng({point[0]}, {point[1]})" for point in points])
    updated_content = outline.replace("LIST_OF_POINTS", google_points).replace("API_KEY", API_KEY).replace(
        "INIT_LATITUDE", INITIAL_LATITUDE).replace("INIT_LONGITUDE", INITIAL_LONGITUDE).replace("INIT_ZOOM", INITIAL_ZOOM)
    f.write(updated_content)
    f.close()


if __name__ == '__main__':
    main()
