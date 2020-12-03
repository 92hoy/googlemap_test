import pandas as pd
import gmplot 
df1 = pd.read_excel("AI_TEST_201104.xlsx")
df1.head()
print (df1)

latitude_list = [ 37.658, 37.877, 37.955] 
longitude_list = [ 127.379, 127.678, 127.685 ] 
gmap3 = gmplot.GoogleMapPlotter(37.658, 
                                127.379, 13) 
  

gmap3.scatter( latitude_list, longitude_list, '#FF0000', 
                              size = 40, marker = True ) 
  
# Plot method Draw a line in 
# between given coordinates 
gmap3.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 2.5) 
# # import gmplot package 
# import gmplot 
  
# latitude_list = [ 37.658, 37.877, 37.955] 
# longitude_list = [ 127.379, 127.678, 127.685 ] 
  
# gmap3 = gmplot.GoogleMapPlotter(38.098, 127.709, 13) 
  
# # scatter method of map object  
# # scatter points on the google map 
# gmap3.scatter( latitude_list, longitude_list, '#FF0000',size = 40, marker = False ) 
  
# # Plot method Draw a line in 
# # between given coordinates 
# gmap3.plot(latitude_list, longitude_list,  
#            'cornflowerblue', edge_width = 2.5) 
  
gmap3.draw('map2.html')