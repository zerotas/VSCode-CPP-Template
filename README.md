# VSCode-CPP-Template
VSCode中C++项目的通用工程模板，方便快捷的实现编译、调试功能  
使用GCC编译器

## 配置
### 软件安装
* MinGW-W64 (适用于Windows用户，Linux用户无视)  
    在Windows系统中使用GCC作为编译器，因此需要MinGW-W64

* CMake
    使用CMake生成MakeFile，并执行编译

* Python
    编写build.py来配置并执行cmake命令

### VSCode插件安装
* C/C++
* Include Autocomplete
* CMake  
  该插件只用于为编写CMakeList.txt提供便利，包括高亮显示、函数提示等  
  我们并不适用该插件来执行cmake命令

### 路径配置
* 配置环境变量，将MinGW-W64/bin添加到Path中
* c_cpp_properties.json中的 compilerPath 配置为g++.exe的绝对路径
* launch.json中的 miDebuggerPath 配置为g++.exe的绝对路径

## 使用
### 开始新项目
复制Template目录，并将Template目录名修改为工程名称即可

### 编译、调试和运行
* Ctrl + Shift + R 选择task执行  
    tasks.json中共配置了5个task，分别为：  
    * build(debug):   
      编译debug版本，编译的可执行文件在bin/debug目录下   
    * build(release):  
      编译debug版本，编译的可执行文件在bin/release目录下   
    * run(debug):  
      执行bin/debug目录的可执行文件  
    * run(release):  
      执行bin/relase目录的可执行文件
    * clean  
      清理编译结果：删除build目录下的所有内容，已经bin/debug，bin/release下的可执行文件

* F5调试  
    在调试前，会自动执行build(debug)的task，生成最新的debug版本

### 关于.vscode目录
该目录下是C/C++插件的配置文件，共有四个文件  

* c_cpp_properties.json  
  该配置文件用于设置代码显示的语法检查、代码跳转  
  例如: 在main.cpp中 
  ```
  #include "include1.h" 
  ```
  编辑器会提示无法找到include1.h文件，我们需要在该配置文件的includePath字段中填写include1.h所在的路径  
  我们在工程中为了方便，使用 ${workspaceFolder}/src/** 来包含src下的所有子目录

  注意：这里配置的头文件搜索路径，只与代码提示有关，与编译无关  
  编译时的头文件搜索路径在CMakeList.txt中配置

  同理
  ```
  "compilerPath": "C:/MinGW/bin/g++.exe",
  "cStandard": "c11",
  "cppStandard": "c++11"
  ```
  文件中配置的编译器信息也只用于语法检查、代码提示等功能，与编译无关
  编译时的相关设置在CMakeList.txt中配置
  

* launch.json  
  该配置文件用于设置调试相关的信息，其中最主要的字段是：
  ```
  "program": "${workspaceFolder}/bin/debug/${workspaceRootFolderName}.exe",
  "miDebuggerPath":"c:/MinGW/bin/gdb.exe",     
  ```
  分别指定调试的exe文件和调试器

* settings.json  
  一般配置信息，无须赘述

* tasks.json  
  该配置文件中指定了5个task，参考上面的"编译、调试和运行"