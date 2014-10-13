EMSINA-VIC AllHazardsSymbology Beta
===================

Build Tools For EMINSA All Hazards Symbology
http://emsinagroup.blogspot.com.au/p/emsina-outputs.html

Integration of build tools to create relevant files automatically from the base SVG files and customisations for Victoria.


Using techniques from the maki project to automatically generate the symbol sets
https://github.com/mapbox/maki
http://www.sjjb.co.uk/mapicons/contactsheet

Complete:
Render to PNG, EMG
ArcGIS Style

Partial:
Font creation, SVG Fonts









Tools and links

Inkscape Full Version Version
http://www.inkscape.org/en/download/windows/
Add inkscape path to PATH environment variable.


http://fontforge.org/
fontforge -c 'font = fontforge.open("./font/$(FONT_NAME).svg"); font.generate("./font/$(FONT_NAME).ttf")'

font = TTFont("C:\code\git\AllHazardsSymbology\ESRI_AllHazards2012\AAHS FIRE.TTF")
font = TTFont("AAHS FIRE.TTF")

font.saveXML("C:\code\git\AllHazardsSymbology\render")

inkscape

for /r %%i in (*.eps) do inkscape.exe --export-png "test.png" "test.svg"


http://www.xnview.com/en/xnconvert/

ImageMagick
http://www.imagemagick.org/script/binary-releases.php#windows


Tools for viewing & developing
http://geojson.io/about.html
