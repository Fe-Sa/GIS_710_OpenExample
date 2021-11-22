import rasterio

with rasterio.open("http://fatra.cnr.ncsu.edu/us-iale2017/US_elevation.tif") as dem:
    print(dem.crs)
    
dem = rasterio.open("http://fatra.cnr.ncsu.edu/us-iale2017/US_elevation.tif")
array = dem.read(1)
from matplotlib import pyplot
%matplotlib inline
pyplot.imshow(array, cmap='pink')
pyplot.show()
