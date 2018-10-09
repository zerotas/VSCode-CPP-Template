# VSCode-CPP-Template
VSCode中C++项目的通用工程模板，方便快捷的实现编译、调试功能
使用GCC编译器

## 配置
### 软件安装
* MinGW-W64 (适用于Windows用户，Linux用户无视)
    在Windows系统中使用GCC作为编译器，因此需要MinGW-W64

* Python
    我们自己编写build.py来执行编译指令

### VSCode插件安装
* C/C++
* Include Autocomplete

### 路径配置
* 配置环境变量，将MinGW-W64/bin添加到Path中
* c_cpp_properties.json中的 compilerPath 配置为g++.exe的绝对路径
* launch.json中的 miDebuggerPath 配置为g++.exe的绝对路径


## 使用
### 编译、调试和运行
* Ctrl + Shift + R 选择task执行
    tasks.json中共配置了4个task，分别为：
        build(debug):   编译debug版本，编译的可执行文件在bin/debug目录下 
        build(release): 编译debug版本，编译的可执行文件在bin/release目录下 
        run(debug):     执行bin/debug目录的可执行文件
        run(release):   执行bin/relase目录的可执行文件

* F5调试
    在调试前，会自动执行build(debug)的task，生成最新的可调试版本

### 开发
    编译时，build.py会扫描src目录下的所有子目录，并将其添加到include path中，因此在代码中include无需添加相对路径，直接使用文件名即可。当然，添加相对路径也可以
    另外，在编译时build.py会扫描src目录下的所有cpp文件，并编译

    上面两点保证了无需手动添加头文件路径和需要编译的cpp文件，这也是我们使用build.py脚本的原因，为编译过程提供了极大的灵活性，比如在编译时可以先删除可执行文件（现在没有这功能）

