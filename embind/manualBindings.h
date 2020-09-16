class_<NCollection_BaseList>("NCollection_BaseList")
  .function("Extent", &NCollection_BaseList::Extent)
  .function("IsEmpty", &NCollection_BaseList::IsEmpty)
  .function("Allocator", &NCollection_BaseList::Allocator)
;
class_<TopTools_ListOfShape, base<NCollection_BaseList>>("TopTools_ListOfShape")
  .constructor<>()
  .constructor<Handle_NCollection_BaseAllocator&>()
  .function("Size", &TopTools_ListOfShape::Size)
  .function("Assign", static_cast<TopTools_ListOfShape& (TopTools_ListOfShape::*) (const TopTools_ListOfShape&) >((TopTools_ListOfShape& (TopTools_ListOfShape::*)(const TopTools_ListOfShape&) ) &TopTools_ListOfShape::Assign))
  .function("operator_assign", static_cast<TopTools_ListOfShape& (TopTools_ListOfShape::*) (const TopTools_ListOfShape&) >((TopTools_ListOfShape& (TopTools_ListOfShape::*)(const TopTools_ListOfShape&) ) &TopTools_ListOfShape::operator=))
  .function("Clear", &TopTools_ListOfShape::Clear)
  .function("First_1", static_cast<const TopoDS_Shape& (TopTools_ListOfShape::*) () const>((const TopoDS_Shape& (TopTools_ListOfShape::*)() const) &TopTools_ListOfShape::First))
  .function("First_2", static_cast<TopoDS_Shape& (TopTools_ListOfShape::*) () >((TopoDS_Shape& (TopTools_ListOfShape::*)() ) &TopTools_ListOfShape::First))
  .function("Last_1", static_cast<const TopoDS_Shape& (TopTools_ListOfShape::*) () const>((const TopoDS_Shape& (TopTools_ListOfShape::*)() const) &TopTools_ListOfShape::Last))
  .function("Last_2", static_cast<TopoDS_Shape& (TopTools_ListOfShape::*) () >((TopoDS_Shape& (TopTools_ListOfShape::*)() ) &TopTools_ListOfShape::Last))
  .function("Append_1", static_cast<TopoDS_Shape& (TopTools_ListOfShape::*) (const TopoDS_Shape&) >((TopoDS_Shape& (TopTools_ListOfShape::*)(const TopoDS_Shape&) ) &TopTools_ListOfShape::Append))
  // .function("Append_2", ...)
  .function("Append_3", static_cast<void (TopTools_ListOfShape::*) (TopTools_ListOfShape&) >((void (TopTools_ListOfShape::*)(TopTools_ListOfShape&) ) &TopTools_ListOfShape::Append))
  .function("Prepend_1", static_cast<TopoDS_Shape& (TopTools_ListOfShape::*) (const TopoDS_Shape&) >((TopoDS_Shape& (TopTools_ListOfShape::*)(const TopoDS_Shape&) ) &TopTools_ListOfShape::Prepend))
  .function("Prepend_2", static_cast<void (TopTools_ListOfShape::*) (TopTools_ListOfShape&) >((void (TopTools_ListOfShape::*)(TopTools_ListOfShape&) ) &TopTools_ListOfShape::Prepend))
  .function("RemoveFirst", &TopTools_ListOfShape::RemoveFirst)
  // .function("Remove_1", ...)
  // .function("Remove_2", ...)
  // .function("InsertBefore_1", ...)
  // .function("InsertBefore_2", ...)
  // .function("InsertAfter_1", ...)
  // .function("InsertAfter_2", ...)
  .function("Reverse", &TopTools_ListOfShape::Reverse)
  // .function("Contains", ...)
;

class_<TColgp_Array1OfDir>("TColgp_Array1OfDir")
  .function("begin", &TColgp_Array1OfDir::begin)
  .function("end", &TColgp_Array1OfDir::end)
  .function("cbegin", &TColgp_Array1OfDir::cbegin)
  .function("cend", &TColgp_Array1OfDir::cend)
  .function("Init", &TColgp_Array1OfDir::Init)
  .function("Size", &TColgp_Array1OfDir::Size)
  .function("Length", &TColgp_Array1OfDir::Length)
  .function("IsEmpty", &TColgp_Array1OfDir::IsEmpty)
  .function("Lower", &TColgp_Array1OfDir::Lower)
  .function("Upper", &TColgp_Array1OfDir::Upper)
  .function("IsDeletable", &TColgp_Array1OfDir::IsDeletable)
  .function("IsAllocated", &TColgp_Array1OfDir::IsAllocated)
  .function("Assign", &TColgp_Array1OfDir::Assign)
  .function("Move", &TColgp_Array1OfDir::Move)
  // .function("operator_assign", &TColgp_Array1OfDir::operator=)
  .function("First", &TColgp_Array1OfDir::First)
  .function("ChangeFirst", &TColgp_Array1OfDir::ChangeFirst)
  .function("Last", &TColgp_Array1OfDir::Last)
  .function("ChangeLast", &TColgp_Array1OfDir::ChangeLast)
  .function("Value", &TColgp_Array1OfDir::Value)
  // .function("operator()_1", ...)
  // .function("operator[]_1", ...)
  .function("ChangeValue", &TColgp_Array1OfDir::ChangeValue)
  // .function("operator()_2", ...)
  // .function("operator[]_2", ...)
  .function("SetValue", &TColgp_Array1OfDir::SetValue)
  .function("Resize", &TColgp_Array1OfDir::Resize)
;
  struct TColgp_Array1OfDir_1 : public TColgp_Array1OfDir {
    TColgp_Array1OfDir_1() : TColgp_Array1OfDir() {}
  };
  class_<TColgp_Array1OfDir_1, base<TColgp_Array1OfDir>>("TColgp_Array1OfDir_1")
    .constructor<>()
  ;
  struct TColgp_Array1OfDir_2 : public TColgp_Array1OfDir {
    TColgp_Array1OfDir_2(const Standard_Integer theLower, const Standard_Integer theUpper) : TColgp_Array1OfDir(theLower, theUpper) {}
  };
  class_<TColgp_Array1OfDir_2, base<TColgp_Array1OfDir>>("TColgp_Array1OfDir_2")
    .constructor<const Standard_Integer, const Standard_Integer>()
  ;
  struct TColgp_Array1OfDir_3 : public TColgp_Array1OfDir {
    TColgp_Array1OfDir_3(const TColgp_Array1OfDir& theOther) : TColgp_Array1OfDir(theOther) {}
  };
  class_<TColgp_Array1OfDir_3, base<TColgp_Array1OfDir>>("TColgp_Array1OfDir_3")
    .constructor<const TColgp_Array1OfDir&>()
  ;
