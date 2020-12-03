import pandas as pd
import gmplot 
import webbrowser
from IPython.display import IFrame

df = pd.read_excel("AI_TEST_201104.xlsx",sheet_name = '03_자동측정망')
# print (df1['이름'])
# print (df1['TM_XAXS'])
# print (df1['TM_YAXS'])
# print (df1['SN'])
# print (df1['N_SN'])
df1 = df['SN'] != 0
df2 = df['N_SN'] != 0
df1 = df[df1]
df2 = df[df2]

X1=[]
Y1=[]
for i in df1['TM_XAXS']:
    X1.append(i)

for i in df1['TM_YAXS']:
    Y1.append(i)

X2=[]
Y2=[]
for i in df2['TM_XAXS']:
    X2.append(i)

for i in df2['TM_YAXS']:
    Y2.append(i)
latitude_list1 = X1
longitude_list1 = Y1

latitude_list2 = X2
longitude_list2 = Y2

gmap1 = gmplot.GoogleMapPlotter(37.87691340116111, 127.6780014421773, 13)
gmap2 = gmplot.GoogleMapPlotter(37.47683764223752, 127.35473560405816, 13)
  
gmap1.scatter( latitude_list1, longitude_list1, '#FF0000',size = 40, marker = True ) 
gmap1.plot(latitude_list1, longitude_list1,'cornflowerblue', edge_width = 2.5) 
gmap1.scatter( latitude_list2, longitude_list2, '#FFFFFF',size = 40, marker = True ) 
gmap1.plot(latitude_list2, longitude_list2,'cornflowerblue', edge_width = 2.5) 
gmap1.draw('map1.html')


# IFrame(src='map1.html', width=700, height=600)
webbrowser.open_new("map1.html")
# gmap2.scatter( latitude_list2, longitude_list2, '#FFFFFF',size = 40, marker = True ) 
# gmap2.plot(latitude_list2, longitude_list2,'cornflowerblue', edge_width = 2.5) 
# gmap2.draw('map2.html')
  
# IPython.display.HTML(open('map1.html').read())
# IPython.display.HTML(open('map2.html').read())
