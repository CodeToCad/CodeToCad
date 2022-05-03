import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))

from textToBlender import *

# scene().setDefaultUnit(BlenderLength.MILLIMETERS)

# curve("legExtrudePath").createLine("5in").rotate("0,0,90d")
# curve("stackingCutoutExtrudePath").createLine("1in").rotate("0,0,90d")

# curve("ellipseLeg").createEllipse("14mm", "27mm") \
#     .sweep("extrudePath", False) \
#     .thicken("5mm") \
#     .landmark("top","center,max,center")\
#     .landmark("bottom","center,min,center")

# curve("ellipseLegOuterCutout").createEllipse("14+3mm", "27+3mm") \
#     .sweep("stackingCutoutExtrudePath", False) \
#     .thicken("5mm") \
#     .landmark("bottom","center,min,center")

# joint("ellipseLeg", "ellipseLegOuterCutout", "bottom", "bottom").transformLandmarkOntoAnother()

# curve("ellipseLeg").subtract("ellipseLegOuterCutout")

shape("ellipseLeg").primitive("cylinder", "1,1,1").remesh().apply()
shape("ellipseLeg").scale("20+3mm,34+3mm,5in")
shape("ellipseLegInner").primitive("cylinder", "1,1,1").remesh().apply()
shape("ellipseLegInner").scale("20mm,34mm,6in")

shape("ellipseLeg").subtract("ellipseLegInner")
shape("ellipseLeg").landmark("top", "center,center,max")

scene().setShapeVisibility("ellipseLegInner", False)
shape("ellipseLegCutout").primitive("cylinder", "1,1,1")
shape("ellipseLegCutout").scale("20+5mm,34+5mm,1in")
shape("ellipseLegCutoutInner").primitive("cylinder", "1,1,1")
shape("ellipseLegCutoutInner").scale("20+2mm,34+2mm,2in")

shape("ellipseLegCutout").subtract("ellipseLegCutoutInner").apply()
shape("ellipseLegCutout").landmark("top", "center,center,max")

scene().setShapeVisibility("ellipseLegCutoutInner", False)

joint("ellipseLeg", "ellipseLegCutout", "top", "top").transformLandmarkOntoAnother()

shape("ellipseLeg").subtract("ellipseLegCutout")

scene().setShapeVisibility("ellipseLegCutout", False)
