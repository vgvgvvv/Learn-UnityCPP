# coding=utf-8

#用于处理生成的swig类的工具

import os
import re

interfacePath = "#C++生成的CS接口的文件夹"
swigObjectHelperPath = "生成的SwigObjectHelper.cs的路径"
filelist = os.listdir(interfacePath)

#######################################################################################################################################
#处理导出文件
class swigCSFile:
    def __init__(self, file):
        self.fileName = file.replace(".cs", "")
        self.className = self.fileName
        self.path = interfacePath + file
        temp = open(path, "r")
        txt = temp.read()
        #是否有析构函数
        self.canDelete =  txt.count("C++ destructor does not have public access") == 0
        #是否能够Dispose
        self.isClass =  txt.count("class") != 0
        temp.close()
    def readlines(self):
        temp = open(path, "r")
        lines = temp.readlines()
        temp.close()
        return lines
    def write(self, txt):
        temp = open(path, "w")
        temp.write(txt)
        temp.close()

# 处理文件
def handleFile(path, csFile):
    codeLines = []
    
    for line in csFile.readlines():
        handleLine(line, codeLines, csFile)
        
    txt = ""
    for line in codeLines:
        txt = txt + line

    csFile.write(txt)
    del csFile  

#处理行
def handleLine(line, codeLines, csFile):
    handleCheckClass(line, csFile)
    if handleGetPtr(line, codeLines, csFile):
        return
    if handleDispose(line, codeLines, csFile):
        return
    if handlePool(line, codeLines, csFile):
        return
    codeLines.append(line)

#获取className及判断是否有c++继承类
classNamePattern = re.compile(r'class (\S*) (.*)')
def handleCheckClass(line, csFile):
    swigClassNameMatch = classNamePattern.search(line)
    if swigClassNameMatch:
        groups = swigClassNameMatch.groups()
        csFile.className = groups[0]
        csFile.isBasicClass = groups[1].count(":") == 0 or groups[1].count("global") != 0

#处理获取指针问题
getPtrPattern = re.compile(r'(internal static.*HandleRef getCPtr)')
def handleGetPtr(line, codeLines, csFile):
    getPtrMatch = getPtrPattern.search(line)
    if getPtrMatch:
        if csFile.isBasicClass:
            codeLines.append("  public global::System.Runtime.InteropServices.HandleRef getPtr() {\n")
        else:
            codeLines.append("  public new global::System.Runtime.InteropServices.HandleRef getPtr() {\n")
        codeLines.append("    return getCPtr(this);\n  }\n\n")
        codeLines.append(line)
        return True
    return False
    
#释放问题
swigPtr2NullPattern = re.compile(r'swigCPtr =.*HandleRef\(null, global::System.IntPtr.Zero\)')
def handleDispose(line, codeLines, csFile):
    swigPtr2NullMatch = swigPtr2NullPattern.search(line)
    if swigPtr2NullMatch:
        line = line.replace("new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero)", "rogamelibsPINVOKE.NULL_HANDLEREF")
        codeLines.append(line)
        return True
    return False

#处理池问题
def handlePool(line, codeLines, csFile):
    fileName = csFile.className
    swigObjPoolPattern = re.compile('public {0}\(global::System.IntPtr cPtr, bool cMemoryOwn\)'.format(fileName))
    swigObjPoolMatch = swigObjPoolPattern.search(line)
    if swigObjPoolMatch:
        codeLines.append("  private readonly static System.Collections.Generic.Queue<{0}> objPool = new System.Collections.Generic.Queue<{0}>();\n\n".format(fileName))

        if csFile.isBasicClass:
            codeLines.append("  public void ReturnPool() {\n")
        else:
            codeLines.append("  public new void ReturnPool() {\n")
        codeLines.append("    if (swigCPtr.Handle != global::System.IntPtr.Zero) {\n")
        codeLines.append("      if (swigCMemOwn) {\n")
        codeLines.append("        swigCMemOwn = false;\n")
        if(csFile.canDelete):
            codeLines.append("        rogamelibsPINVOKE.delete_{0}(swigCPtr);\n".format(fileName))
        else:
            codeLines.append("        throw new global::System.MethodAccessException(\"C++ destructor does not have public access\");\n")
        codeLines.append("      }\n")
        codeLines.append("      swigCPtr = rogamelibsPINVOKE.NULL_HANDLEREF;\n")
        codeLines.append("    }\n")
        codeLines.append("    objPool.Enqueue(this);\n")
        codeLines.append("  }\n\n")

        if csFile.isBasicClass:
            codeLines.append("  public static {0} GetFromPool(global::System.Runtime.InteropServices.HandleRef swigCPtr, bool cMemoryOwn) {{\n".format(fileName))
        else:
            codeLines.append("  public static new {0} GetFromPool(global::System.Runtime.InteropServices.HandleRef swigCPtr, bool cMemoryOwn) {{\n".format(fileName))
        codeLines.append("    if (objPool.Count > 0) {\n")
        codeLines.append("      var obj = objPool.Dequeue();\n")
        codeLines.append("      obj.swigCPtr = swigCPtr;\n")
        codeLines.append("      obj.swigCMemOwn = cMemoryOwn;\n")
        codeLines.append("      return obj;\n")
        codeLines.append("    }\n")
        codeLines.append("    return new {0}(swigCPtr.Handle, cMemoryOwn);\n".format(fileName))
        codeLines.append("  }\n\n")

        if csFile.isBasicClass:
            codeLines.append("  public static void ClearPool() {\n")
        else:
            codeLines.append("  public static new void ClearPool() {\n")
        codeLines.append("    while (objPool.Count > 0) {\n")
        codeLines.append("      objPool.Dequeue().Dispose();\n")
        codeLines.append("    }\n")
        codeLines.append("  }\n\n")
        codeLines.append(line)
        return True
    swigObjPoolPattern2 = re.compile('public {0}\(global::System.IntPtr cPtr, bool futureUse\)'.format(fileName))
    swigObjPoolMatch2 = swigObjPoolPattern2.search(line)
    if swigObjPoolMatch2:
        codeLines.append("  private readonly static System.Collections.Generic.Queue<{0}> objPool = new System.Collections.Generic.Queue<{0}>();\n\n".format(fileName))

        codeLines.append("  public void ReturnPool() {\n")
        codeLines.append("    if (swigCPtr.Handle != global::System.IntPtr.Zero) {\n")
        codeLines.append("      swigCPtr = rogamelibsPINVOKE.NULL_HANDLEREF;\n")
        codeLines.append("    }\n")
        codeLines.append("    objPool.Enqueue(this);\n")
        codeLines.append("  }\n\n")

        codeLines.append("  public static {0} GetFromPool(global::System.Runtime.InteropServices.HandleRef swigCPtr, bool futureUse) {{\n".format(fileName))
        codeLines.append("    if (objPool.Count > 0) {\n")
        codeLines.append("      var obj = objPool.Dequeue();\n")
        codeLines.append("      obj.swigCPtr = swigCPtr;\n")
        codeLines.append("      return obj;\n")
        codeLines.append("    }\n")
        codeLines.append("    return new {0}(swigCPtr.Handle, futureUse);\n".format(fileName))
        codeLines.append("  }\n\n")

        codeLines.append("  public static void ClearPool() {\n")
        codeLines.append("    objPool.Clear();\n")
        codeLines.append("  }\n\n")
        codeLines.append(line)
        return True
    return False

#######################################################################################################################################
#添加SwigObjectHelper
class swigHelperFile:
    def __init__(self):
        self.path = swigObjectHelperPath
        self.helperFile = open(swigObjectHelperPath, "w")
        self.fileList = []
        self.codeLines = []
    def close(self):
        self.helperFile.close()

    def createSwigHelper(self):

        self.codeLines.append("namespace ROGameLibs\n")
        self.codeLines.append("{\n")
        self.codeLines.append("  public class SwigObjectHelper\n")
        self.codeLines.append("  {\n")

        self.createCleanPool()

        self.codeLines.append("  }\n")
        self.codeLines.append("}\n")

        self.helperFile.writelines(self.codeLines)

    def createCleanPool(self):
        self.codeLines.append("      public static void ClearPool()\n")
        self.codeLines.append("      {\n")
        for fileName in self.fileList:
            self.codeLines.append("         " + fileName.replace(".cs", "") + ".ClearPool();\n")
                
        self.codeLines.append("      }\n")

#######################################################################################################################################
#执行操作
swigHelper = swigHelperFile()

for file in filelist :
    if file.count("rogamelibs") != 0:
        continue
    path = interfacePath + file
    csFile = swigCSFile(file)
    if csFile.isClass :
        swigHelper.fileList.append(csFile.fileName)
    handleFile(path, csFile)
    

swigHelper.createSwigHelper()
swigHelper.close()
