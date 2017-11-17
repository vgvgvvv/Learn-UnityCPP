//------------------------------------------------------------------------------
// <auto-generated />
//
// This file was automatically generated by SWIG (http://www.swig.org).
// Version 3.0.12
//
// Do not make changes to this file unless you know what you are doing--modify
// the SWIG interface file instead.
//------------------------------------------------------------------------------


public class UnsignedCharArray : global::System.IDisposable {
  private global::System.Runtime.InteropServices.HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal UnsignedCharArray(global::System.IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new global::System.Runtime.InteropServices.HandleRef(this, cPtr);
  }

  internal static global::System.Runtime.InteropServices.HandleRef getCPtr(UnsignedCharArray obj) {
    return (obj == null) ? new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero) : obj.swigCPtr;
  }

  ~UnsignedCharArray() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != global::System.IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          swiglibPINVOKE.delete_UnsignedCharArray(swigCPtr);
        }
        swigCPtr = new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero);
      }
      global::System.GC.SuppressFinalize(this);
    }
  }

  public UnsignedCharArray(int nelements) : this(swiglibPINVOKE.new_UnsignedCharArray(nelements), true) {
  }

  public byte getitem(int index) {
    byte ret = swiglibPINVOKE.UnsignedCharArray_getitem(swigCPtr, index);
    return ret;
  }

  public void setitem(int index, byte value) {
    swiglibPINVOKE.UnsignedCharArray_setitem(swigCPtr, index, value);
  }

  public SWIGTYPE_p_unsigned_char cast() {
    global::System.IntPtr cPtr = swiglibPINVOKE.UnsignedCharArray_cast(swigCPtr);
    SWIGTYPE_p_unsigned_char ret = (cPtr == global::System.IntPtr.Zero) ? null : new SWIGTYPE_p_unsigned_char(cPtr, false);
    return ret;
  }

  public static UnsignedCharArray frompointer(SWIGTYPE_p_unsigned_char t) {
    global::System.IntPtr cPtr = swiglibPINVOKE.UnsignedCharArray_frompointer(SWIGTYPE_p_unsigned_char.getCPtr(t));
    UnsignedCharArray ret = (cPtr == global::System.IntPtr.Zero) ? null : new UnsignedCharArray(cPtr, false);
    return ret;
  }

}
