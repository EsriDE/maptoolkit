from arcgis.features import FeatureSet, GeoAccessor
from glob import glob
import json
import pandas as pd


def read_geojson_as_sdf(filepath: str):
    """
    Reads a GeoJSON file as spatially enabled dataframe.
    
    :param filepath: The local path to the GeoJSON file.
    """
    with open(filepath, mode="r", encoding="utf8") as in_stream:
        return FeatureSet.from_geojson(json.load(in_stream)).sdf
    
def read_csv_files_as_sdf(csv_files_pattern: str, x_column: str, y_column: str, sr: int = 4326, nrows: int = None):
    """
    Reads multiple CSV files as a spatially enabled dataframe.

    :param csv_files_pattern: The file pattern e.g. /home/dev/data/AIS/AIS_*.csv
    :param x_column: The name of the X-coordinate series.        
    :param y_column: The name of the Y-coordinate series.
    :param sr: The wkid number of the spatial reference.
    :param nrows: The maximum number of rows to read for each file.
    """
    df = pd.concat(map(lambda filepath: pd.read_csv(filepath, nrows=nrows), glob(csv_files_pattern)), ignore_index=True)
    return GeoAccessor.from_xy(df, x_column=x_column, y_column=y_column, sr=sr)