import os
from osgeo import gdal

CROP_CMD = 'gdal_translate -srcwin %s %s %s %s %s %s'
# % (xoff, yoff, xsize, ysize, src, dst)


def crop(raster_filename, chunk_size=244, crop_dir='/tmp/'):
    """
    Given a raster, a chunk size, and a directory to write into...
    Break the raster up into chunks of the appropriate size.
    """
    ds = gdal.Open(raster_filename)
    numPixelsWide, numPixelsHigh = ds.RasterXSize, ds.RasterYSize
    for x in range(0, numPixelsWide-chunk_size-1, chunk_size):
        for y in range(0, numPixelsHigh-chunk_size-1, chunk_size):
            chunk_filename = os.path.join(crop_dir, '%s-%s.tif' % (x, y))
            os.system(CROP_CMD % (
                x, y, chunk_size, chunk_size, raster_filename, chunk_filename
            ))
