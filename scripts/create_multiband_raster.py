import rasterio
print('all modules imported')

# path to the sentinel rasters
raster_base_path = "/Users/hk/Downloads/Sentinel2_Kurs2/Uebungen/JaehrlicheVeraenderungen/sentinel2/S2A_MSIL1C_20180704T103021_N0206_R108_T32TLT_20180704T174024.SAFE/GRANULE/L1C_T32TLT_A015835_20180704T103023/IMG_DATA/"

# output path
output_base_path = "/Users/hk/Downloads/gaga/"

# initialize the rasters to have in the multiband result.
band2 = rasterio.open(raster_base_path + "T32TLT_20180704T103021_B02.jp2", driver="JP2OpenJPEG")  # blue
band3 = rasterio.open(raster_base_path + "T32TLT_20180704T103021_B03.jp2", driver="JP2OpenJPEG")  # green
band4 = rasterio.open(raster_base_path + "T32TLT_20180704T103021_B04.jp2", driver="JP2OpenJPEG")  # red
band8 = rasterio.open(raster_base_path + "T32TLT_20180704T103021_B08.jp2", driver="JP2OpenJPEG")  # nir

# print out metadata about the rasters
print(band4.count)  # number of raster bands
print(band4.width)  # row count
print(band4.height) # column count
print(band4.dtypes) # data type of the raster
print(band4.crs)    # projection of the raster

print("create multiband image...")
# create a new (empty) raster
multiband = rasterio.open(output_base_path + "multiband.tiff", "w", driver="Gtiff", width=band2.width,
                          height=band2.height, count=4, crs=band2.crs, transform=band2.transform, dtype=band2.dtypes[0])

# write the bands to the multiband raster
multiband.write(band8.read(1),4) # nir
multiband.write(band2.read(1),3) # blue
multiband.write(band3.read(1),2) # green
multiband.write(band4.read(1),1) # red
multiband.close()

print("create false color image...")
# empty raster space for a falseColor image
falseColor = rasterio.open(output_base_path + "falschfarben.tiff", "w", driver="Gtiff", width=band2.width,
                          height=band2.height, count=3, crs=band2.crs, transform=band2.transform, dtype=band2.dtypes[0])

# write the bands to the falseColor raster
falseColor.write(band8.read(1),1) # nir
falseColor.write(band2.read(1),2) # green
falseColor.write(band3.read(1),3) # blue
falseColor.close()

print("finished")
