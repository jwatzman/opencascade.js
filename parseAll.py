#!/usr/bin/python3.8

import subprocess
import os

occtFiles = [
  # BRep
  "BRep_Builder.hxx",
  "BRep_Curve3D.hxx",
  "BRep_CurveOn2Surfaces.hxx",
  "BRep_CurveOnClosedSurface.hxx",
  "BRep_CurveOnSurface.hxx",
  "BRep_CurveRepresentation.hxx",
  "BRep_GCurve.hxx",
  "BRep_ListIteratorOfListOfCurveRepresentation.hxx",
  "BRep_ListIteratorOfListOfPointRepresentation.hxx",
  "BRep_ListOfCurveRepresentation.hxx",
  "BRep_ListOfPointRepresentation.hxx",
  "BRep_PointOnCurve.hxx",
  "BRep_PointOnCurveOnSurface.hxx",
  "BRep_PointOnSurface.hxx",
  "BRep_PointRepresentation.hxx",
  "BRep_PointsOnSurface.hxx",
  "BRep_Polygon3D.hxx",
  "BRep_PolygonOnClosedSurface.hxx",
  "BRep_PolygonOnClosedTriangulation.hxx",
  "BRep_PolygonOnSurface.hxx",
  "BRep_PolygonOnTriangulation.hxx",
  "BRep_TEdge.hxx",
  "BRep_TFace.hxx",
  "BRep_Tool.hxx",
  "BRep_TVertex.hxx",

  # BRepAlgoAPI
  "BRepAlgoAPI_Algo.hxx",
  "BRepAlgoAPI_BooleanOperation.hxx",
  "BRepAlgoAPI_BuilderAlgo.hxx",
  "BRepAlgoAPI_Check.hxx",
  "BRepAlgoAPI_Common.hxx",
  "BRepAlgoAPI_Cut.hxx",
  "BRepAlgoAPI_Defeaturing.hxx",
  "BRepAlgoAPI_Fuse.hxx",
  "BRepAlgoAPI_Section.hxx",
  "BRepAlgoAPI_Splitter.hxx",

  # BRepBuilderAPI
  "BRepBuilderAPI_BndBoxTreeSelector.hxx",
  "BRepBuilderAPI_CellFilter.hxx",
  "BRepBuilderAPI_Collect.hxx",
  "BRepBuilderAPI_Command.hxx",
  "BRepBuilderAPI_Copy.hxx",
  "BRepBuilderAPI_EdgeError.hxx",
  "BRepBuilderAPI_FaceError.hxx",
  "BRepBuilderAPI_FastSewing.hxx",
  "BRepBuilderAPI_FindPlane.hxx",
  "BRepBuilderAPI_GTransform.hxx",
  "BRepBuilderAPI.hxx",
  "BRepBuilderAPI_MakeEdge2d.hxx",
  "BRepBuilderAPI_MakeEdge.hxx",
  "BRepBuilderAPI_MakeFace.hxx",
  "BRepBuilderAPI_MakePolygon.hxx",
  "BRepBuilderAPI_MakeShape.hxx",
  "BRepBuilderAPI_MakeShell.hxx",
  "BRepBuilderAPI_MakeSolid.hxx",
  "BRepBuilderAPI_MakeVertex.hxx",
  "BRepBuilderAPI_MakeWire.hxx",
  "BRepBuilderAPI_ModifyShape.hxx",
  "BRepBuilderAPI_NurbsConvert.hxx",
  "BRepBuilderAPI_PipeError.hxx",
  "BRepBuilderAPI_Sewing.hxx",
  "BRepBuilderAPI_ShapeModification.hxx",
  "BRepBuilderAPI_ShellError.hxx",
  "BRepBuilderAPI_Transform.hxx",
  "BRepBuilderAPI_TransitionMode.hxx",
  "BRepBuilderAPI_VertexInspector.hxx",
  "BRepBuilderAPI_WireError.hxx",

  # BRepFilletAPI
  "BRepFilletAPI_LocalOperation.hxx",
  "BRepFilletAPI_MakeChamfer.hxx",
  "BRepFilletAPI_MakeFillet2d.hxx",
  "BRepFilletAPI_MakeFillet.hxx",

  # BRepLib
  "BRepLib_CheckCurveOnSurface.hxx",
  "BRepLib_Command.hxx",
  "BRepLib_EdgeError.hxx",
  "BRepLib_FaceError.hxx",
  "BRepLib_FindSurface.hxx",
  "BRepLib_FuseEdges.hxx",
  "BRepLib.hxx",
  "BRepLib_MakeEdge2d.hxx",
  "BRepLib_MakeEdge.hxx",
  "BRepLib_MakeFace.hxx",
  "BRepLib_MakePolygon.hxx",
  "BRepLib_MakeShape.hxx",
  "BRepLib_MakeShell.hxx",
  "BRepLib_MakeSolid.hxx",
  "BRepLib_MakeVertex.hxx",
  "BRepLib_MakeWire.hxx",
  "BRepLib_ShapeModification.hxx",
  "BRepLib_ShellError.hxx",
  "BRepLib_WireError.hxx",

  # BRepOffsetAPI
  "BRepOffsetAPI_DraftAngle.hxx",
  "BRepOffsetAPI_FindContigousEdges.hxx",
  "BRepOffsetAPI_MakeDraft.hxx",
  "BRepOffsetAPI_MakeEvolved.hxx",
  "BRepOffsetAPI_MakeFilling.hxx",
  "BRepOffsetAPI_MakeOffset.hxx",
  "BRepOffsetAPI_MakeOffsetShape.hxx",
  "BRepOffsetAPI_MakePipe.hxx",
  "BRepOffsetAPI_MakePipeShell.hxx",
  "BRepOffsetAPI_MakeThickSolid.hxx",
  "BRepOffsetAPI_MiddlePath.hxx",
  "BRepOffsetAPI_NormalProjection.hxx",
  "BRepOffsetAPI_SequenceOfSequenceOfReal.hxx",
  "BRepOffsetAPI_SequenceOfSequenceOfShape.hxx",
  "BRepOffsetAPI_Sewing.hxx",
  "BRepOffsetAPI_ThruSections.hxx",

  # BRepPrimAPI
  "BRepPrimAPI_MakeBox.hxx",
  "BRepPrimAPI_MakeCone.hxx",
  "BRepPrimAPI_MakeCylinder.hxx",
  "BRepPrimAPI_MakeHalfSpace.hxx",
  "BRepPrimAPI_MakeOneAxis.hxx",
  "BRepPrimAPI_MakePrism.hxx",
  "BRepPrimAPI_MakeRevol.hxx",
  "BRepPrimAPI_MakeRevolution.hxx",
  "BRepPrimAPI_MakeSphere.hxx",
  "BRepPrimAPI_MakeSweep.hxx",
  "BRepPrimAPI_MakeTorus.hxx",
  "BRepPrimAPI_MakeWedge.hxx",

  "Geom_Axis1Placement.hxx",
  "Geom_Axis2Placement.hxx",
  "Geom_AxisPlacement.hxx",
  "Geom_BezierCurve.hxx",
  "Geom_BezierSurface.hxx",
  "Geom_BoundedCurve.hxx",
  "Geom_BoundedSurface.hxx",
  "Geom_BSplineCurve.hxx",
  "Geom_BSplineSurface.hxx",
  "Geom_CartesianPoint.hxx",
  "Geom_Circle.hxx",
  "Geom_ConicalSurface.hxx",
  "Geom_Conic.hxx",
  "Geom_Curve.hxx",
  "Geom_CylindricalSurface.hxx",
  "Geom_Direction.hxx",
  "Geom_ElementarySurface.hxx",
  "Geom_Ellipse.hxx",
  "Geom_Geometry.hxx",
  "Geom_HSequenceOfBSplineSurface.hxx",
  "Geom_Hyperbola.hxx",
  "Geom_Line.hxx",
  "Geom_OffsetCurve.hxx",
  "Geom_OffsetSurface.hxx",
  "Geom_OsculatingSurface.hxx",
  "Geom_Parabola.hxx",
  "Geom_Plane.hxx",
  "Geom_Point.hxx",
  "Geom_RectangularTrimmedSurface.hxx",
  "Geom_SequenceOfBSplineSurface.hxx",
  "Geom_SphericalSurface.hxx",
  "Geom_Surface.hxx",
  "Geom_SurfaceOfLinearExtrusion.hxx",
  "Geom_SurfaceOfRevolution.hxx",
  "Geom_SweptSurface.hxx",
  "Geom_ToroidalSurface.hxx",
  "Geom_Transformation.hxx",
  "Geom_TrimmedCurve.hxx",
  "Geom_UndefinedDerivative.hxx",
  "Geom_UndefinedValue.hxx",
  "Geom_Vector.hxx",
  "Geom_VectorWithMagnitude.hxx",

  # Geom2d
  "Geom2d_AxisPlacement.hxx",
  "Geom2d_BezierCurve.hxx",
  "Geom2d_BoundedCurve.hxx",
  "Geom2d_BSplineCurve.hxx",
  "Geom2d_CartesianPoint.hxx",
  "Geom2d_Circle.hxx",
  "Geom2d_Conic.hxx",
  "Geom2d_Curve.hxx",
  "Geom2d_Direction.hxx",
  "Geom2d_Ellipse.hxx",
  "Geom2d_Geometry.hxx",
  "Geom2d_Hyperbola.hxx",
  "Geom2d_Line.hxx",
  "Geom2d_OffsetCurve.hxx",
  "Geom2d_Parabola.hxx",
  "Geom2d_Point.hxx",
  "Geom2d_Transformation.hxx",
  "Geom2d_TrimmedCurve.hxx",
  "Geom2d_UndefinedDerivative.hxx",
  "Geom2d_UndefinedValue.hxx",
  "Geom2d_Vector.hxx",
  "Geom2d_VectorWithMagnitude.hxx",

  # GC
  "GC_MakeArcOfCircle.hxx",
  "GC_MakeArcOfEllipse.hxx",
  "GC_MakeArcOfHyperbola.hxx",
  "GC_MakeArcOfParabola.hxx",
  "GC_MakeCircle.hxx",
  "GC_MakeConicalSurface.hxx",
  "GC_MakeCylindricalSurface.hxx",
  "GC_MakeEllipse.hxx",
  "GC_MakeHyperbola.hxx",
  "GC_MakeLine.hxx",
  "GC_MakeMirror.hxx",
  "GC_MakePlane.hxx",
  "GC_MakeRotation.hxx",
  "GC_MakeScale.hxx",
  "GC_MakeSegment.hxx",
  "GC_MakeTranslation.hxx",
  "GC_MakeTrimmedCone.hxx",
  "GC_MakeTrimmedCylinder.hxx",
  "GC_Root.hxx",

  # GCE2d
  "GCE2d_MakeArcOfCircle.hxx",
  "GCE2d_MakeArcOfEllipse.hxx",
  "GCE2d_MakeArcOfHyperbola.hxx",
  "GCE2d_MakeArcOfParabola.hxx",
  "GCE2d_MakeCircle.hxx",
  "GCE2d_MakeEllipse.hxx",
  "GCE2d_MakeHyperbola.hxx",
  "GCE2d_MakeLine.hxx",
  "GCE2d_MakeMirror.hxx",
  "GCE2d_MakeParabola.hxx",
  "GCE2d_MakeRotation.hxx",
  "GCE2d_MakeScale.hxx",
  "GCE2d_MakeSegment.hxx",
  "GCE2d_MakeTranslation.hxx",
  "GCE2d_Root.hxx",

  # gp
  "gp_Ax1.hxx",
  "gp_Ax22d.hxx",
  "gp_Ax2d.hxx",
  "gp_Ax2.hxx",
  "gp_Ax3.hxx",
  "gp_Circ2d.hxx",
  "gp_Circ.hxx",
  "gp_Cone.hxx",
  "gp_Cylinder.hxx",
  "gp_Dir2d.hxx",
  "gp_Dir.hxx",
  "gp_Elips2d.hxx",
  "gp_Elips.hxx",
  "gp_EulerSequence.hxx",
  "gp_GTrsf2d.hxx",
  "gp_GTrsf.hxx",
  "gp.hxx",
  "gp_Hypr2d.hxx",
  "gp_Hypr.hxx",
  "gp_Lin2d.hxx",
  "gp_Lin.hxx",
  "gp_Mat2d.hxx",
  "gp_Mat.hxx",
  "gp_Parab2d.hxx",
  "gp_Parab.hxx",
  "gp_Pln.hxx",
  "gp_Pnt2d.hxx",
  "gp_Pnt.hxx",
  "gp_Quaternion.hxx",
  "gp_QuaternionNLerp.hxx",
  "gp_QuaternionSLerp.hxx",
  "gp_Sphere.hxx",
  "gp_Torus.hxx",
  "gp_Trsf2d.hxx",
  "gp_TrsfForm.hxx",
  "gp_Trsf.hxx",
  "gp_TrsfNLerp.hxx",
  "gp_Vec2d.hxx",
  "gp_Vec.hxx",
  "gp_VectorWithNullMagnitude.hxx",
  "gp_XY.hxx",
  "gp_XYZ.hxx",

  # STEPControl
  "STEPControl_ActorRead.hxx",
  "STEPControl_ActorWrite.hxx",
  "STEPControl_Controller.hxx",
  "STEPControl_Reader.hxx",
  "STEPControl_StepModelType.hxx",
  "STEPControl_Writer.hxx",

  # TopExp
  "TopExp_Explorer.hxx",
  "TopExp.hxx",
  "TopExp_Stack.hxx",

  # TopoDS
  "TopoDS_AlertWithShape.hxx",
  "TopoDS_Builder.hxx",
  "TopoDS_Compound.hxx",
  "TopoDS_CompSolid.hxx",
  "TopoDS_Edge.hxx",
  "TopoDS_Face.hxx",
  "TopoDS_FrozenShape.hxx",
  "TopoDS_HShape.hxx",
  "TopoDS.hxx",
  "TopoDS_Iterator.hxx",
  "TopoDS_ListIteratorOfListOfShape.hxx",
  "TopoDS_ListOfShape.hxx",
  "TopoDS_LockedShape.hxx",
  "TopoDS_Shape.hxx",
  "TopoDS_Shell.hxx",
  "TopoDS_Solid.hxx",
  "TopoDS_TCompound.hxx",
  "TopoDS_TCompSolid.hxx",
  "TopoDS_TEdge.hxx",
  "TopoDS_TFace.hxx",
  "TopoDS_TShape.hxx",
  "TopoDS_TShell.hxx",
  "TopoDS_TSolid.hxx",
  "TopoDS_TVertex.hxx",
  "TopoDS_TWire.hxx",
  "TopoDS_UnCompatibleShapes.hxx",
  "TopoDS_Vertex.hxx",
  "TopoDS_Wire.hxx",

  "TopTools_Array1OfListOfShape.hxx",
  "TopTools_Array1OfShape.hxx",
  "TopTools_Array2OfShape.hxx",
  "TopTools_DataMapIteratorOfDataMapOfIntegerListOfShape.hxx",
  "TopTools_DataMapIteratorOfDataMapOfIntegerShape.hxx",
  "TopTools_DataMapIteratorOfDataMapOfOrientedShapeInteger.hxx",
  "TopTools_DataMapIteratorOfDataMapOfOrientedShapeShape.hxx",
  "TopTools_DataMapIteratorOfDataMapOfShapeInteger.hxx",
  "TopTools_DataMapIteratorOfDataMapOfShapeListOfInteger.hxx",
  "TopTools_DataMapIteratorOfDataMapOfShapeListOfShape.hxx",
  "TopTools_DataMapIteratorOfDataMapOfShapeReal.hxx",
  "TopTools_DataMapIteratorOfDataMapOfShapeSequenceOfShape.hxx",
  "TopTools_DataMapIteratorOfDataMapOfShapeShape.hxx",
  "TopTools_DataMapOfIntegerListOfShape.hxx",
  "TopTools_DataMapOfIntegerShape.hxx",
  "TopTools_DataMapOfOrientedShapeInteger.hxx",
  "TopTools_DataMapOfOrientedShapeShape.hxx",
  "TopTools_DataMapOfShapeBox.hxx",
  "TopTools_DataMapOfShapeInteger.hxx",
  "TopTools_DataMapOfShapeListOfInteger.hxx",
  "TopTools_DataMapOfShapeListOfShape.hxx",
  "TopTools_DataMapOfShapeReal.hxx",
  "TopTools_DataMapOfShapeSequenceOfShape.hxx",
  "TopTools_DataMapOfShapeShape.hxx",
  "TopTools_HArray1OfListOfShape.hxx",
  "TopTools_HArray1OfShape.hxx",
  "TopTools_HArray2OfShape.hxx",
  "TopTools_HSequenceOfShape.hxx",
  "TopTools.hxx",
  "TopTools_IndexedDataMapOfShapeAddress.hxx",
  "TopTools_IndexedDataMapOfShapeListOfShape.hxx",
  "TopTools_IndexedDataMapOfShapeReal.hxx",
  "TopTools_IndexedDataMapOfShapeShape.hxx",
  "TopTools_IndexedMapOfOrientedShape.hxx",
  "TopTools_IndexedMapOfShape.hxx",
  "TopTools_ListIteratorOfListOfShape.hxx",
  "TopTools_ListOfListOfShape.hxx",
  "TopTools_ListOfShape.hxx",
  "TopTools_LocationSet.hxx",
  "TopTools_LocationSetPtr.hxx",
  "TopTools_MapIteratorOfMapOfOrientedShape.hxx",
  "TopTools_MapIteratorOfMapOfShape.hxx",
  "TopTools_MapOfOrientedShape.hxx",
  "TopTools_MapOfShape.hxx",
  "TopTools_MutexForShapeProvider.hxx",
  "TopTools_OrientedShapeMapHasher.hxx",
  "TopTools_SequenceOfShape.hxx",
  "TopTools_ShapeMapHasher.hxx",
  "TopTools_ShapeSet.hxx"
]

for occtFile in occtFiles:
  moduleName = occtFile.split('_')[0]
  if moduleName == occtFile:
    moduleName = os.path.splitext(occtFile)[0]
  inputFile = "./build/occt/src/" + moduleName + "/" + occtFile
  if not os.path.exists("./embind/" + moduleName):
    os.makedirs("./embind/" + moduleName)
  outputFile = "./embind/" + moduleName + "/" + os.path.splitext(occtFile)[0] + ".h"
  subprocess.call(['./parse.py', inputFile, outputFile])
