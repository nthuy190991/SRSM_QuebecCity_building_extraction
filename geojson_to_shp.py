#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:18:42 2020

@author: thanhhuy nguyen, eric janssens-coron
"""

import datetime
import geopandas as gpd

INDIR = ""
OUTDIR = INDIR

#%% Convert an ERSI Shapefile to GeoJSON
FILE = "Quebec.geojson.shp"

SCRIPT_START_TIME = datetime.datetime.now()
print("Started at: " + str(datetime.datetime.now()))
GDFB = gpd.read_file(INDIR + FILE)

print(GDFB.head())
GDFB.to_file(driver='GeoJSON', filename=OUTDIR + FILE + '.geojson')

print()
print("Duration: " + str(datetime.datetime.now() - SCRIPT_START_TIME))
print()
print("Ended at: " + str(datetime.datetime.now()))

#%% Convert GeoJSON into an ERSI Shapefile
FILE = "QC_footprints.geojson"

SCRIPT_START_TIME = datetime.datetime.now()
print("Started at: " + str(datetime.datetime.now()))
GDFB = gpd.read_file(INDIR + FILE)

print(GDFB.head())
GDFB.to_file(driver='ESRI Shapefile', filename=OUTDIR + FILE + '.shp')

print()
print("Duration: " + str(datetime.datetime.now() - SCRIPT_START_TIME))
print()
print("Ended at: " + str(datetime.datetime.now()))
