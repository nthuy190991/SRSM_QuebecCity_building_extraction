# Quebec City building footprints extracted by SRSM 
Delineated building footprints in Quebec City (Canada), resulted by the SRSM method (Super-Resolution-based Snake Model). The dataset covers a total area is **656 square kilometers, with more than 200 thousand buildings**.

These building footprints are the results of our paper **Super-Resolution-based Snake Model --- An Unsupervised Method for Large-Scale Building Extraction using Airborne LiDAR Data and Optical Image**.

Authors: [Thanh Huy Nguyen](mailto:nthuy190991@gmail.com), Sylvie Daniel, Didier Guériot, Christophe Sintès, and Jean-Marc Le Caillec.

## Download links
[Raw SRSM results]()
(in case that the link expires, please open an issue on the Issues tracker or [email me](mailto:nthuy190991@gmail.com)).

## Citation
If you use these footprints, please cite our paper:
```
  {bibtex}
```

## Conversion ERSI Shapefile into GeoJSON
In order to convert [ERSI Shapefile](https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf) into [GeoJSON](https://geojson.org) or vice versa, please use the Python script 'geojson_to_shp.py' (credits to Dr. Eric Janssens-Coron from CRDIG, Université Laval). Prerequisite for this Python script is [Geopandas](https://geopandas.org).

## What is the coordinate reference system?
[EPSG: 2949](https://epsg.io/2949) a.k.a. NAD83(CSRS) / MTM zone 7

## Notes:
- For the sake of computational cost, we carried out the SRSM separately on tile (each covers a 1 square km)
- The tile-based results were then combined in QGIS
- Two versions are provided: without and with built-in polygonization. But only the raw results (from SRSM) are used in the publication.

## Questions/Discussions
For any other questions/issues, please open an issue on the Issues tracker.
