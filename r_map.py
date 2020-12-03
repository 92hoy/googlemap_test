import pandas as pd
import gmplot 
import webbrowser
from IPython.display import IFrame

# df = pd.read_excel("AI_TEST_201104.xlsx",sheet_name = '03_자동측정망')

SN_x_list=[37.658, 37.877, 37.955, 38.098]
SN_y_list=[127.379, 127.678, 127.685, 127.709]
N_SN_x_list=[37.442, 37.507]
N_SN_y_list=[127.31, 127.451]


# gmap1 = gmplot.GoogleMapPlotter(37.87691340116111, 127.6780014421773, 13)
# gmap2 = gmplot.GoogleMapPlotter(37.47683764223752, 127.35473560405816, 13)
  
# gmap1.scatter( SN_x_list, SN_y_list, '#FFFFFF',size = 40, marker = True ) 
# gmap1.plot(SN_x_list, SN_y_list,'cornflowerblue', edge_width = 2.5) 

# gmap1.scatter( N_SN_x_list, N_SN_y_list, '#FFFFFF',size = 40, marker = True ) 
# gmap1.plot(N_SN_x_list, N_SN_y_list,'cornflowerblue', edge_width = 2.5) 
#상류
# gmap1.scatter( [37.658, 37.877, 37.955, 38.098], [127.379, 127.678, 127.685, 127.709], '#0000FF',size = 40, marker = True ) 
# gmap1.plot([37.658, 37.877, 37.955, 38.098], [127.379, 127.678, 127.685, 127.709],'fuchsia', edge_width = 2.0) 
# 상류
# gmap1.scatter( [37.658, 37.877, 37.955], [127.379, 127.678, 127.685], '#0000FF',size = 40, marker = True ) 
# gmap1.plot([37.658, 37.877, 37.955], [127.379, 127.678, 127.685],'fuchsia', edge_width = 2.0) 
# 상류
# gmap1.scatter( [37.658, 37.877], [127.379, 127.678], '#0000FF',size = 40, marker = True ) 
# gmap1.plot([37.658, 37.877], [127.379, 127.678],'fuchsia', edge_width = 2.0)
#하류
# gmap1.scatter( [37.658], [127.379], '#FFFF00',size = 40, marker = True ) 

# 상류
# gmap1.scatter( [ 37.877, 37.955, 38.098], [ 127.678, 127.685, 127.709], '#0000FF',size = 40, marker = True ) 
# gmap1.plot([ 37.877, 37.955, 38.098], [ 127.678, 127.685, 127.709],'fuchsia', edge_width = 2.0)  
# 상류
# gmap1.scatter( [ 37.877, 37.955], [ 127.678, 127.685], '#0000FF',size = 40, marker = True ) 
# gmap1.plot([ 37.877, 37.955], [ 127.678, 127.685],'fuchsia', edge_width = 2.0)  
#하류
# gmap1.scatter( [37.877], [127.678], '#FFFF00',size = 40, marker = True ) 

#상류
# gmap1.scatter( [37.955, 38.098], [127.685, 127.709], '#0000FF',size = 40, marker = True ) 
# gmap1.plot([37.955, 38.098], [127.685, 127.709],'fuchsia', edge_width = 2.0) 
#하류
# gmap1.scatter( [37.955], [127.685], '#FFFF00',size = 40, marker = True ) 

#상류
# gmap1.scatter([37.442, 37.507],[127.31, 127.451], '#0000FF',size = 40, marker = True ) 
# gmap1.plot([37.442, 37.507],[127.31, 127.451],'fuchsia', edge_width = 2.0) 
#하류
# gmap1.scatter( [37.442], [127.31], '#FFFF00',size = 40, marker = True)




gmap3 = gmplot.GoogleMapPlotter(36.23597327066295, 128.35082091806157, 12)
#상류
gmap3.scatter([36.193567,36.273154],[128.36276,128.34578], '#0000FF',size = 40, marker = True ) 
gmap3.plot([36.193567,36.273154],[128.36276,128.34578],'fuchsia', edge_width = 2.0) 
#하류
gmap3.scatter( [36.193567], [128.36276], '#FFFF00',size = 40, marker = True)

gmap3.draw('map9.html')
