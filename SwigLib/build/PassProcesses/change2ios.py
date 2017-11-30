#coding=utf-8

#用于处理生成的PIVOKE文件，用于处理IOS库问题
import re
import os

fh = open("生成的swiglibsPINVOKE.cs的路径", 'r')

arr = []
pattern = re.compile(r'("swiglibs.*En.*")')
pattern2 = re.compile(r'"(CSharp_SwigLibs_.*)"')
pattern3 = re.compile(r'jarg[1-9]')

print("start")
isFunction = False
fullFuncName = ""

lineNumber = 0
for i in fh.readlines():

    lineNumber = lineNumber + 1

    if lineNumber == 14:
        arr.append("    public static readonly global::System.Runtime.InteropServices.HandleRef NULL_HANDLEREF = new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero);\n")

    if lineNumber == 36 or lineNumber == 104:
        arr.append("#if UNUSED \n")
    if lineNumber == 55 or lineNumber == 123:
        arr.append("#endif \n")
    
    if lineNumber == lineNumber == 167:
        arr.append("#if UNUSED \n")

    if lineNumber == lineNumber == 185:
        arr.append("#else \n")
        arr.append("#if !UNITY_IOS && !UNITY_ANDROID \n")
        arr.append("  [System.Runtime.InteropServices.UnmanagedFunctionPointer(System.Runtime.InteropServices.CallingConvention.Cdecl)]  \n")
        arr.append("#endif \n")
        arr.append("  public delegate string SWIGStringDelegate(string message); \n")
        arr.append("  static SWIGStringDelegate stringDelegate = new SWIGStringDelegate(CreateString); \n\n")
        arr.append("#if UNITY_IOS \n")
        arr.append('  [global::System.Runtime.InteropServices.DllImport("__Internal")] \n')
        arr.append("#else \n")
        arr.append('  [global::System.Runtime.InteropServices.DllImport("swiglibs", EntryPoint="SWIGRegisterStringCallback_swiglibs")] \n')
        arr.append("#endif \n")
        arr.append("  public static extern void SWIGRegisterStringCallback_swiglibs(SWIGStringDelegate stringDelegate);\n")
        arr.append("  [AOT.MonoPInvokeCallback(typeof(SWIGStringDelegate))]\n")
        arr.append("  static string CreateString(string cString) { return cString; }\n")
        arr.append("#endif \n")
    
    if lineNumber == 188:
        arr.append("    SWIGRegisterStringCallback_swiglibs(stringDelegate);\n")

    if isFunction:
        match3 = pattern3.findall(i)

        arr.append("#if UNITY_IOS \n")
        shortFuncName = fullFuncName.replace("CSharp_SwigLibs_", "")
        externFunc = i.replace(shortFuncName, fullFuncName) 
        interfaceFunc = i.replace("extern ", "").replace(";", "")

        arr.append(externFunc + "\n")
        arr.append(interfaceFunc + "  {\n")

        if externFunc.count("void") == 0 :
            arr.append("    return ")
        else:
            arr.append("    ")
        arr.append(fullFuncName + "(")
        argNum = 0
        for arg in match3:
            if argNum != 0:
                arr.append(", ")
            arr.append(arg)
            argNum = argNum + 1
        arr.append(");\n")

        arr.append("  }\n")
        arr.append("#else\n")
        arr.append(i)
        arr.append("#endif" + '\n')

        fullFuncName = ""
        isFunction = False
        continue

    match1 = pattern.search(i)
    match2 = pattern2.search(i)
    if match1 and not match2:
        arr.append("#if UNITY_IOS \n")
        new = i.replace(match1.group(), '"__Internal"')
        arr.append(new)
        arr.append("#else\n")
        arr.append(i)
        arr.append("#endif" + '\n')
    elif match1 and match2:
        arr.append("#if UNITY_IOS \n")
        new = i.replace(match1.group(), '"__Internal"')
        fullFuncName = match2.group(1)
        arr.append(new)
        arr.append("#else\n")
        arr.append(i)
        arr.append("#endif" + '\n')
        isFunction = True
    else:
        arr.append(i)
    
    

fh.close()

txt = ""
for i in arr:
    txt = txt + i

fh = open("生成的swiglibsPINVOKE.cs的路径", 'w')
fh.write(txt)
fh.close()
