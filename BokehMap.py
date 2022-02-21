## import 
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
import os 

def plot(lat, lng, zoom=10, map_type='roadmap'):

   os.environ["GOOGLE_API_KEY"] = 'AIzaSyCHqZYVSJau7_qVmDdAtG5BY3v7sRa4eC0' # google api key  
   api_key = os.environ['GOOGLE_API_KEY']

   gmap_options = GMapOptions(lat=lat[4], lng=lng[4], map_type=map_type, zoom=zoom)

   # Bokeh googleMap 연동 
   p = gmap(api_key, gmap_options, title='Pays de Gex', 
            tools=['hover', 'reset', 'wheel_zoom', 'pan'])

   # 데이터 
   source = ColumnDataSource(
        data=dict(lat=lat,
                  lon=lng)
        )
   
   # 범례 example 
   for _,col in zip(range(3),["yellow","blue","purple"]):
        p.circle(x = 'lon', y = 'lat', size=10, alpha=0.8, color=col, source=source, legend_label=col)
    

   p.legend.location = "top_right"
   p.legend.orientation = "horizontal"
   p.legend.click_policy="hide"
   
   return p

def main():

    lat, lon = [], []

    # jeju.txt 예시로 실행 
    with open("./jeju.txt", "r",encoding='UTF8') as f:
        lines = f.readlines()
        
        for l in lines:
            cit, la, lo = l.strip().split(",")
            lat.append(float(la))
            lon.append(float(lo))

    p = plot(lat, lon, map_type='roadmap', zoom=9)

    return p

if __name__ == "__main__":

    main()    
