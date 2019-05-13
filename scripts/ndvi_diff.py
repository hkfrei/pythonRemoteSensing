import numpy
import rasterio
import gdal
print('all modules imported')

# path to the folder with the ndvi rasters
base_path = "/Users/hk/Downloads/gaga/"

# shapefile with forest mask
forest_mask = base_path + "waldmaske_wgs84.shp"

# initialize the necessary rasters for the ndvi calculation.
ndvi_2017 = rasterio.open(base_path + "ndvi_17.tiff", driver="GTiff")
ndvi_2018 = rasterio.open(base_path + "ndvi_18.tiff", driver="GTiff")

# print out metadata about the ndvi's
print(ndvi_2018.count)  # number of raster bands
print(ndvi_2017.count)  # number of raster bands
print(ndvi_2018.height)  # column count
print(ndvi_2018.dtypes)  # data type of the raster e.g. ('float64',)
print(ndvi_2018.crs)  # projection of the raster e.g. EPSG:32632

print("calculate ndvi difference")
# this is will give us an array of values, not an actual raster image.
ndvi_diff_array = numpy.subtract(ndvi_2018.read(1), ndvi_2017.read(1))

print("reclassify")
# reclassify
ndvi_diff_reclass_array = numpy.where(
    ndvi_diff_array <= -0.05, 1, 9999.0
)

# create a new (empty) raster for the "original" diff
ndvi_diff_image = rasterio.open(base_path + "ndvi_diff.tif", "w", driver="Gtiff", width=ndvi_2018.width,
                                height=ndvi_2018.height, count=1, crs=ndvi_2018.crs, transform=ndvi_2018.transform,
                                dtype='float64')

# create a new (empty) raster for the reclassified diff
ndvi_diff_reclass_image = rasterio.open(base_path + "ndvi_reclass_diff.tif", "w", driver="Gtiff", width=ndvi_2018.width,
                                        height=ndvi_2018.height, count=1, crs=ndvi_2018.crs,
                                        transform=ndvi_2018.transform, dtype='float64')

# write the ndvi's to raster
ndvi_diff_image.write(ndvi_diff_array.astype("float64"), 1)
ndvi_diff_reclass_image.write(ndvi_diff_reclass_array.astype("float64"), 1)
ndvi_diff_image.close()
ndvi_diff_reclass_image.close()

# extract forest areas
# Make sure to add correct Nodata and Alpha values. They have to match the reclassified values.
warp_options = gdal.WarpOptions(cutlineDSName=forest_mask, cropToCutline=True, dstNodata=9999, dstAlpha=9999)
gdal.Warp(base_path + "change_masked.tif", base_path + "ndvi_reclass_diff.tif", options=warp_options)

print("finished")
