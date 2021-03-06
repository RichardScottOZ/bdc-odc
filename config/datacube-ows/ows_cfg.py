# BANDS
## Alias for band names
bands_cbers = {
    "BAND13": ["blue"],
    "BAND14": ["green"],
    "BAND15": ["red"],
    "BAND16": ["nir"],
    "CLEAROB": ["ClearOb"],
    "EVI": ["evi"],
    "NDVI": ["ndvi"],
    "PROVENANCE": ["Provenance"],
    "TOTALOB": ["TotalOb"]
}

bands_ls = {
    "band1": ["coastal"],
    "band2": ["blue"],
    "band3": ["green"],
    "band4": ["red"],
    "band5": ["nir"],
    "band6": ["swir1", "shortwave_infrared_1", "near_shortwave_infrared"],
    "band7": ["swir2", "shortwave_infrared_2", "far_shortwave_infrared"],
    "CLEAROB": ["ClearOb"],
    "EVI": ["evi"],
    "NDVI": ["ndvi"],
    "PROVENANCE": ["Provenance"],
    "TOTALOB": ["TotalOb"]
}

bands_s2 = {
    "band1": ["coastal"],
    "band2": ["blue"],
    "band3": ["green"],
    "band4": ["red"],
    "band5": ["rededge1"],
    "band6": ["rededge2"],
    "band7": ["rededge3"],
    "band8": ["nir"],
    "band8a": ["nir08"],
    "band11": ["swir16", ],
    "band12": ["swir22"],
    "CLEAROB": ["ClearOb"],
    "EVI": ["evi"],
    "NDVI": ["ndvi"],
    "PROVENANCE": ["Provenance"],
    "TOTALOB": ["TotalOb"]
}

# RESLIM
reslim_cbers = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 10,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
    }
}

reslim_landsat = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 10,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    }
}

reslim_s2 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 10,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
    }
}

# STYLES
# STYLES
style_cbers_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {
        "red": {
            "BAND15": 1.0
        },
        "green": {
            "BAND14": 1.0
        },
        "blue": {
            "BAND13": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_ls8_simple_rgb = {
    "name": "simple_ls8_rgb",
    "title": "Simple LS8 RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {
        "red": {
            "band4": 1.0
        },
        "green": {
            "band3": 1.0
        },
        "blue": {
            "band2": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_s2_simple_rgb = {
    "name": "simple_s2_rgb",
    "title": "Simple S2 RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {
        "red": {
            "band4": 1.0
        },
        "green": {
            "band3": 1.0
        },
        "blue": {
            "band2": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

# MAIN BDC's CONFIGURATION OBJECT
ows_cfg = {
    "global": {
        # Master config for all services and products.
        "response_headers": {
            "Access-Control-Allow-Origin": "*",  # CORS header
        },
        "services": {
            "wms": True,
            "wcs": True,
            "wmts": True,
        },
        "published_CRSs": {
            # TODO: UPDATE to CBERS's CRSs
            "EPSG:3857": {  # Web Mercator
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3577": {  # GDA-94
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:32623": {  # WGS 84 / UTM zone 23N
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:4326": {  # WGS-84
                "geographic": True,
                "vertical_coord_first": True
            },
            "EPSG:6933": {  # Cylindrical equal area
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "ESRI:102022": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "+proj=aea +lat_0=-12 +lon_0=-54 +lat_1=-2 +lat_2=-22 +x_0=5000000 +y_0=10000000 +ellps=GRS80 +units=m +no_defs": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y"
            },
            "+proj=aea +lat_1=-1 +lat_2=-29 +lat_0=0 +lon_0=-54 +x_0=0 +y_0=0 +ellps=GRS80 +units=m +no_defs +type=crs": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y"
            },
            "+proj=aea +lat_1=-1 +lat_2=-29 +lat_0=0 +lon_0=-54 +x_0=0 +y_0=0 +ellps=GRS80 +units=m +no_defs": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y"
            }
        },
        "allowed_urls": [
            "https://brazildatacube.dpi.inpe.br/opendatacube/ows/"
        ],
        # Metadata to go straight into GetCapabilities documents
        "title": "Brazil Data Cube - OGC Web Services",
        "abstract": """Brazil Data Cube OGC Web Services""",
        "info_url": "brazildatacube.org/",
        "keywords": [
            "cbers",
            "brazil",
        ],
        "contact_info": {
            "person": "Brazil Data Cube",
            "organisation": "National Institute for Space Research",
            "position": "",
            "address": {
                "type": "postal",
                "address": "Av. dos Astronautas, 1758",
                "city": "São José Dos Campos",
                "state": "São Paulo",
                "postcode": "12227-010",
                "country": "Brazil",
            },
            "telephone": "+55 12 3208 6000",
            "fax": "",
            "email": "gilberto.queiroz@inpe.br",
        },
        "fees": "",
        # TODO: REVIEW LICENSE
        "access_constraints": "This product is released under the Creative Commons Attribution 4.0 International Licence. "
                              "http://creativecommons.org/licenses/by/4.0/legalcode",
    },  # END OF global SECTION
    "wms": {
        # XXX: Defined to default values
        # Provide S3 data URL, bucket name for data_links in GetFeatureinfo responses
        # Note that this feature is currently restricted to data stored in AWS S3.
        # This feature is also fairly specialised to DEA requirements and may not be suited to more general use.
        # All Optional
        "s3_url": "http://data.au",
        "s3_bucket": "s3_bucket_name",
        "s3_aws_zone": "ap-southeast-2",
        # Max tile height/width for wms.  (N.B. Does not apply to WMTS)
        # Optional, defaults to 256x256
        "max_width": 512,
        "max_height": 512,
    },  # END OF wms SECTION
    # TODO: UPDATE WCS
    "wcs": {
        # Config for WCS service, for all products/coverages
        "default_geographic_CRS": "EPSG:4326",
        "native_wcs_format": "GeoTIFF",
        "formats": {
            "GeoTIFF": {
                # "renderer": "datacube_ows.wcs_utils.get_tiff",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_tiff",
                    "2": "datacube_ows.wcs2_utils.get_tiff",
                },
                "mime": "image/geotiff",
                "extension": "tif",
                "multi-time": False
            },
            "netCDF": {
                # "renderer": "datacube_ows.wcs_utils.get_netcdf",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_netcdf",
                    "2": "datacube_ows.wcs2_utils.get_netcdf",
                },
                "mime": "application/x-netcdf",
                "extension": "nc",
                "multi-time": True,
            },
        },
        "native_format": "GeoTIFF",
    },  # END OF wcs SECTION
    "layers": [
        {
            "title": "Brazil Data Cube - OGC Web Services",
            "abstract": "Brazil Data Cube OGC Web Services",
            "layers": [
                # Hierarchical list of layers.  May be a combination of unnamed/unmappable folder-layers or named mappable layers.
                {
                    "title": "Sentinel-2",
                    "abstract": "Sentinel-2 (MSI) Cube Collections (VERSION 1)",
                    "layers": [
                        {
                            "title": "Sentinel-2 (MSI) Cube Stack 16 days - v001",
                            "name": "S2_10_16D_STK_1",
                            "abstract": "Sentinel-2 (MSI) Cube Stack 16 days - v001",
                            "product_name": "S2_10_16D_STK_1",
                            "bands": bands_s2,
                            "resource_limits": reslim_s2,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": True,
                                "fuse_func": "datacube.helpers.ga_pq_fuser",
                                "apply_solar_corrections": False,
                            },
                            "wcs": {
                                "native_crs": "+proj=aea +lat_0=-12 +lon_0=-54 +lat_1=-2 +lat_2=-22 +x_0=5000000 +y_0=10000000 +ellps=GRS80 +units=m +no_defs",
                                "native_resolution": [10, -10],
                                "native_wcs_format": "GeoTIFF",
                                "default_bands": ["band4", "band3", "band2"]
                            },
                            "styling": {
                                "default_style": "simple_s2_rgb",
                                "styles": [
                                    style_s2_simple_rgb
                                ]
                            }
                        }]
                },
                {
                    "title": "Landsat-8",
                    "abstract": "Landsat-8 (OLI) Cube Collections (VERSION 1)",
                    "layers": [
                        {
                            "title": "Landsat-8 (OLI) Cube Stack 16 days - v001",
                            "name": "LC8_30_16D_STK_1",
                            "abstract": "Landsat-8 (OLI) Cube Stack 16 days - v001",
                            "product_name": "LC8_30_16D_STK_1",
                            "bands": bands_ls,
                            "resource_limits": reslim_landsat,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": True,
                                "fuse_func": "datacube.helpers.ga_pq_fuser",
                                "apply_solar_corrections": False,
                            },
                            "wcs": {
                                "native_crs": "+proj=aea +lat_0=-12 +lon_0=-54 +lat_1=-2 +lat_2=-22 +x_0=5000000 +y_0=10000000 +ellps=GRS80 +units=m +no_defs",
                                "native_resolution": [30, -30],
                                "native_wcs_format": "GeoTIFF",
                                "default_bands": ["band4", "band3", "band2"]
                            },
                            "styling": {
                                "default_style": "simple_ls8_rgb",
                                "styles": [
                                    style_ls8_simple_rgb
                                ]
                            }
                        }]
                },
                {
                    "title": "CBERS-4",
                    "abstract": "CBERS4 COLLECTIONS (VERSION 1)",
                    "layers": [
                        {
                            "title": "CBERS-4 (AWFI) Cube Stack 16 days - v001",
                            "name": "CB4_64_16D_STK_1",
                            "abstract": "CBERS-4 (AWFI) Cube Stack 16 days - v001",
                            "product_name": "CB4_64_16D_STK_1",
                            "bands": bands_cbers,
                            "resource_limits": reslim_cbers,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": True,
                                "apply_solar_corrections": False,
                            },
                            "wcs": {
                                "native_crs": "+proj=aea +lat_0=-12 +lon_0=-54 +lat_1=-2 +lat_2=-22 +x_0=5000000 +y_0=10000000 +ellps=GRS80 +units=m +no_defs",
                                "native_resolution": [64, -64],
                                "native_wcs_format": "GeoTIFF",
                                "default_bands": ["BAND15", "BAND14", "BAND13"]
                            },
                            "styling": {
                                "default_style": "simple_rgb",
                                "styles": [
                                    style_cbers_simple_rgb
                                ]
                            }
                        }]
                }]
        }]
}
