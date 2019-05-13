import numpy
import rasterio
print('all modules imported')

# path to the sentinel rasters
raster_base_path = "/Users/hk/Downloads/Sentinel2_Kurs2/Uebungen/JaehrlicheVeraenderungen/sentinel2/S2A_MSIL1C_20170619T103021_N0205_R108_T32TLT_20170619T103021.SAFE/GRANULE/L1C_T32TLT_A010401_20170619T103021/IMG_DATA/"

# output path
output_base_path = "/Users/hk/Downloads/gaga/"

# initialize the necessary rasters for the ndvi calculation.
band4 = rasterio.open(raster_base_path + "T32TLT_20170619T103021_B04.jp2", driver="JP2OpenJPEG")  # red
band8 = rasterio.open(raster_base_path + "T32TLT_20170619T103021_B08.jp2", driver="JP2OpenJPEG")  # nir

# print out metadata about the rasters
print(band4.count)  # number of raster bands
print(band4.width)  # row count
print(band4.height)  # column count
print(band4.dtypes)  # data type of the raster ('uint16',)
print(band4.crs)  # projection of the raster

# because the output of the ndvi is a floating point number,
# we have to convert the input rasters to floating point as well.
red = band4.read(1).astype('float64')
nir = band8.read(1).astype('float64')

print("create ndvi image...")
# this is will give us an array of values, not a real raster image.
ndvi_array = numpy.where(
    # if nir + red equals 0, we want the ndvi to be 0,
    # otherwise there is an error because of division by 0
    (nir + red) == 0., 0,
    # if the value is > 0, we calculate the ndvi
    (nir - red) / (nir + red)
)

# set negative ndvi values to 0, we only want values between 0 and 1.
ndvi_array = numpy.where(ndvi_array < 0, 0, ndvi_array)

# create a new (empty) raster
ndvi_image = rasterio.open(output_base_path + "ndvi_17.tif", "w", driver="Gtiff", width=band4.width,
                           height=band4.height, count=1, crs=band4.crs, transform=band4.transform, dtype='float64')

# write the array to the raster band 1
ndvi_image.write(ndvi_array, 1)
ndvi_image.close()

print("finished")
