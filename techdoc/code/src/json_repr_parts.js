{
  "__type":"model",
  "NrOf": NrOfObj,
  "Sources": SourcesArray,
  "ExternalMasses": ExternalMassesArray
  "Rulers":[],
  "MinMmaxSwitchAngle": <float>,
  "Parameters": ParametersObj
}

//------------------------------------------------

NrOfObj: {
  "__type":"counters",
  "Sources": <int>,
  "ExtremalPoints": <int>,
  "Contours": <int>,
  "ContourPoints": <int>
}

//------------------------------------------------

"Parameters": {
  "pixrad": <int>,
  "n_models": <int>,
  "isSym": <Boolean>,
  "z_src": <int>,
  "z_lens": <float>,
  "orgPxScale": <float>,
  "orgImgSize": <int>,
  "svgViewportSize": <int>,
  "pxScale": <float>
}

//------------------------------------------------

ExternalMassesArray: [ ExtMass1, ExtMass2, ...]

ExtMassX: {
  "__type":"ext_mass",
  "idnr": <int>,
  "x": <float>,
  "y": <float>,
  "r": <float>,
  "phi": <float>,
}

//------------------------------------------------

SourcesArray: [ ExtPnt1, ExtPnt2, ... ]

ExtPntX: {
  "__type":"extpnt",
  "idnr": <int>,
  "x": <float>,
  "y": <float>,
  "depth": <int>,
  "isRoot": <Boolean>,
  "isExpanded": <Boolean>,
  "childrenInsideEachOther": <Boolean>,
  "type": <"sad"|"min"|"max">,
  "wasType": <"sad"|"min"|"max">,
  "child1": ExtPntX1,
  "child2": ExtPntX2,
  "contour": ContourXY
}

//------------------------------------------------

ContourXY: {
  "__type":"contour",
  "idnr": <int>,
  "cpoints": [ CPntXY1, CPntXY2, ... ]
}

//------------------------------------------------

CPntXYZ: {
  "__type":"cpnt",
  "idnr": <int>,
  "r_fac": <float>,
  "d_phi": <float>
}