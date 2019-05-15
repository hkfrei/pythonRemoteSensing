import gdal
import rasterio
print('all modules imported')

# path to input and output raster.
# the input must exist and will be resampled
# the output raster will be generated during this script.
inputRaster = "/Users/hk/Downloads/gaga/ndvi_17.tiff"
outputRaster = "/Users/hk/Downloads/gaga/ndvi_17_resampled.tif"

# cellsize for the output raster
cellsize = 5
resampling_method = "bilinear" # near, bilinear, cubic... see https://www.gdal.org/gdalwarp.html
print("variables set")

# print metadata about the input raster
print("input raster infos:")
raster = rasterio.open(inputRaster, driver="GTiff")
print(raster.count)  # number of raster bands
print(raster.height)  # column count
print(raster.width) # row count
print(raster.dtypes) # data type of the raster e.g. ('float64',)
print(raster.crs)  # projection of the raster e.g. EPSG:32632
print(raster.res) # the current cellsize

raster.close()

print("start resampling...")
# options for the resampling process
warp_options = gdal.WarpOptions(xRes=cellsize, yRes=cellsize, resampleAlg=resampling_method)
# the actual resampling process
gdal.Warp(outputRaster, inputRaster, options=warp_options)

# print metadata about the output raster
print("output raster infos:")
result = rasterio.open(outputRaster, driver="GTiff")
print(result.count)  # number of raster bands
print(result.height)  # column count
print(result.width) # row count
print(result.dtypes) # data type of the raster e.g. ('float64',)
print(result.crs)  # projection of the raster e.g. EPSG:32632
print(result.res) # the current cellsize

result.close()

print("finished")
