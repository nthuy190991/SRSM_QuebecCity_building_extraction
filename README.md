# Quebec City building footprints extracted by SRSM 
Delineated building footprints in Quebec City (Canada), resulted by the SRSM method (Super-Resolution-based Snake Model). The dataset covers a total area is **656 square kilometers, with more than 200 thousand buildings**.

These building footprints are the results of our paper **Super-Resolution-based Snake Model --- An Unsupervised Method for Large-Scale Building Extraction using Airborne LiDAR Data and Optical Image**.

Authors: [Thanh Huy Nguyen](mailto:nthuy190991@gmail.com), Sylvie Daniel, Didier Guériot, Christophe Sintès, and Jean-Marc Le Caillec.

## Download links
[SRSM results](https://ulavaldti-my.sharepoint.com/:u:/g/personal/thngu52_ulaval_ca/EcsaXqiItQFAqF9HxTBc7fQB0bBIndcbUuF3oPzHFFUa0A?e=m4UCCf) (approx. 210 MB).

(in case that the link expires, please open an issue on the Issues tracker or [email me](mailto:nthuy190991@gmail.com))


## Citation
If you use these footprints, please cite our (preprint) paper:
```
@article{nguyen2020super,
  title={Super-Resolution-based Snake Model--An Unsupervised Method for Large-Scale Building Extraction using Airborne LiDAR Data and Optical Image},
  author={Nguyen, Thanh Huy and Daniel, Sylvie and Gueriot, Didier and Sintes, Christophe and Caillec, Jean-Marc Le},
  journal={arXiv preprint arXiv:2004.08522},
  year={2020}
}
```


## Ground Truth (GT) building footprints
The GT footprints of Quebec City are provided by the City of Quebec and updated regularly.
They are used as a reference for evaluating the SRSM results. It is worth-nothing that we don't use them as training data  or use any training data for that matter (hence **unsupervised**).

We would like to thank the City of Quebec for providing and maintaining this dataset.
To download these GT footprints, please refer to their [website](https://www.donneesquebec.ca/recherche/fr/dataset/empreintes-des-batiments).


## Comparison with Microsoft open Canada building footprints
We compared the SRSM results with the open Canada building footprint datasets carried out by Microsoft Bing maps team (see their [blog entry](https://blogs.bing.com/maps/2019-03/microsoft-releases-12-million-canadian-building-footprints-as-open-data) and [Github](https://github.com/microsoft/CanadianBuildingFootprints)). 

### Accuracy metrics
| Area-based | Completeness | Correctness | Quality | F1-score | Notes |
| --- | :---: | :---: | :---: | :---: | --- |
| Microsoft | 77.42 % | 87.61 % | 69.77 % | 82.20 % | Using ResNet34 as the foundation |
| SRSM | 82.32 % | 72.02 % | 62.37 % | 76.73 % | Unsupervised method |
| **Object-based** | **Completeness** | **Correctness** | **Quality** | **F1-score** |  |
| Microsoft | 59.01 % | 93.16 % | 56.56 % | 72.26 % | |
| SRSM | 74.25 % | 80.95 % | 63.21 % | 77.46 % | |


    
## Some examples
SRSM results overlapped on z-image (tile 4190) |  SRSM results overlapped on z-image (tile 4785)
:-------------------------:|:-------------------------:
<img src="https://github.com/nthuy190991/SRSM_QuebecCity_building_extraction/blob/master/examples/4190_on_zimg.png" alt="Tile 4190" width="100%" height="20%"/> | <img src="https://github.com/nthuy190991/SRSM_QuebecCity_building_extraction/blob/master/examples/4785_on_zimg.png" alt="Tile 4785" width="100%" height="20%"/>
**SRSM results overlapped on orthoimage (tile 4190)** |  **SRSM results overlapped on orthoimage (tile 4785)**
 <img src="https://github.com/nthuy190991/SRSM_QuebecCity_building_extraction/blob/master/examples/4190_on_opt_img.png" alt="Tile 4190" width="100%" height="20%"/> | <img src="https://github.com/nthuy190991/SRSM_QuebecCity_building_extraction/blob/master/examples/4785_on_opt_img.png" alt="Tile 4785" width="100%" height="20%"/>
**Ground truth (tile 4190)** |  **Ground truth (tile 4785)**
 <img src="https://github.com/nthuy190991/SRSM_QuebecCity_building_extraction/blob/master/examples/4190_gt.png" alt="Tile 4190" width="85%" height="26%"/> | <img src="https://github.com/nthuy190991/SRSM_QuebecCity_building_extraction/blob/master/examples/4785_gt.png" alt="Tile 4785" width="85%" height="26%"/>

## What is the coordinate reference system?
[EPSG: 2949](https://epsg.io/2949) a.k.a. NAD83(CSRS) / MTM zone 7


## Notes:
- For the sake of computational cost, we carried out the SRSM separately on tile (each covers a 1km x 1km area).
- The tile-based results were then combined in QGIS.
- A version of the simplified footprints by applying the ERSI ArcMap built-in polygonization [algorithm](https://arxiv.org/abs/1504.06584) can be found [here](https://ulavaldti-my.sharepoint.com/:u:/g/personal/thngu52_ulaval_ca/EcNbGxwXWOVFuwV4u8wulhQBRc7sRkT7xnsDjHORgWRibA?e=vLmqNP). But only the raw results from SRSM are used in the publication.


## Conversion ERSI Shapefile into GeoJSON
In order to convert [ERSI Shapefile](https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf) into [GeoJSON](https://geojson.org) or vice versa, please use the Python script 'geojson_to_shp.py' (credits to Dr. Eric Janssens-Coron from CRDIG, Université Laval). Prerequisite: [Geopandas](https://geopandas.org).


## Questions/Discussions
For any other questions/issues, please open an issue on the Issues tracker.
