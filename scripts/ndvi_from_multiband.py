import numpy
import rasterio
print('all modules imported')

# path to the multiband raster
input_base_path = "/Users/hk/Downloads/gaga/multiband.tiff"

# output path
output_base_path = "/Users/hk/Downloads/gaga/"

# open the multiband raster and assign it to a variable
multiband = rasterio.open(input_base_path, driver="GTiff")

# print out metadata about the rasters
print(multiband.count)  # number of raster bands
print(multiband.width)  # row count
print(multiband.height)  # column count
print(multiband.dtypes)  # data type of the raster ('uint16',)
print(multiband.crs)  # projection of the raster

# because the output of the ndvi is a floating point number,
# we have to convert the input rasters to floating point as well.
red = multiband.read(1).astype('float64')
nir = multiband.read(4).astype('float64')

print("create ndvi image...")
# this is will give us an array of values, not yet an actual raster image.
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
ndvi_image = rasterio.open(output_base_path + "ndvi_from_multiband.tiff", "w", driver="Gtiff", width=multiband.width,
                           height=multiband.height, count=1, crs=multiband.crs, transform=multiband.transform, dtype='float64')

# write the array to the raster band 1
ndvi_image.write(ndvi_array, 1)

ndvi_image.close()

print("finished")
