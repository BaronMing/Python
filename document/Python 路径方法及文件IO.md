# Python 路径方法及文件I/O

## 前言

1. 使用`Python`路径方法需要引用`os.path`

    ```python
    # 常规方法
    import os.path
    # 缩减路径
    import os.path as path
    ```



## 第一部分 路径方法

### A：返回路径

#### 获取 绝对路径

> `os.path.abspath(路径)`
>
> 注意如下两点：
>
> - 如果你想通过执行`os.path.abspath(".")`来获取当前文件的路径，那结果可能并不如你所料。`os.path.abspath(".")`返回的是命令执行时用户所在的目录，举例如下：
>
>   ```bash
>   # 这里使用的是 python2 版本，因为CentOS Minimal默认安装的是 python2
>   [root@localhost ~]# vim /tmp/test.py
>   import os.path as path
>   print path.abspath(".")
>   
>   [root@localhost ~] # python /tmp/test.py
>   # 返回值如下（原因是用户是在/root下执行的命令）
>   /root
>   ```
>
> - 参数中的路径一般情况是**相对路径**，但是在编程中，如果不确定你输入的路径是相对路径还是绝对路径，可以用这个方法将其统一化为绝对路径

#### 获取`basename`

> os.path.basename(路径)
>
>  - `/home/baron`，这里的`baron`就是`basename`，也就是路径最后所指向的`文件`或`目录`名称
>
>    （我这里的`文件`和`目录`是`Linux`系统的术语）
>
>  - `/home/baron/`，如果路径类似这样**以`/`结尾**，那该方法**会返回空字符串**

#### 获取`dirname`

> `os.path.dirname(路径)`
>
> - `/home/baron`，去掉`basename`，返回目录路径，这个路径`/home`就是`dirname`。
>
>   `dirname`会同时去掉`basename`前的`/`
>
> - 如果路径是`.`（当前路径），会返回空字符串

#### 获取 公共路径

> `os.path.commonprefix(路径列表)`：例如
>
> ```python
> >>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
> '/usr'
> ```

#### 获取 真实路径

> `os.path.realpath(路径)`
>
> - 这个一般情况下与`os.path.abspath`相同，但是当`realpath`的路径指向的是**符号链接文件**时，会返回链接文件所指向文件的路径
>
>   ```bash
>   [root@localhost ~]# ll
>   total 8
>   -rw-------. 2 root root 1208 Dec 10 23:33 anaconda-ks.cfg
>   -rw-------. 2 root root 1208 Dec 10 23:33 anaconda-ks.cfg.hardlink
>   lrwxrwxrwx  1 root root   15 Dec 12 06:45 anaconda-ks.cfg.link -> anaconda-ks.cfg
>   [root@localhost ~]# python
>   >>> from os.path import realpath
>   >>> realpath("anaconda-ks.cfg.hardlink")
>   '/root/anaconda-ks.cfg.hardlink'
>   >>> realpath("anaconda-ks.cfg.link")
>   '/root/anaconda-ks.cfg'
>   >>> 
>   ```
>
> - **硬链接不会返回硬链接所指向文件的路径**

#### 获取 相对路径

> `os.path.relpath(路径[, 起始点])`
>
> - 从起始点开始计算相对路径

#### 获取 公共路径前缀

> `os.path.commonpath(路径列表)`：例如
>
> ```python
> >>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
> '/usr/l'
> ```
>
> 这个一般是用来做补全功能的吧 ^_^


### B：路径信息判断

#### 判断 路径的指向是否存在

> `os.path.exists(路径)`
>
> `os.path.lexists(路径)`

#### 判断 是否为绝对路径

> `os.path.isabs(路径)`

#### 判断 路径的类型

##### 01 判断 是否为文件

> `os.path.isfile(路径)`

##### 02 判断 是否为目录

> `os.path.isdir(路径)`

##### 03 判断 是否为链接文件

> `os.path.islink(路径)`

##### 04 判断 是否为挂载点

> `os.path.ismount(路径)`

#### 判断 是否支持任意`Unicode`字符

> `os.path.supports_unicode_filenames`
>
> 注意，这个不是一个方法，**不需要括号和参数**。
>
> 在文件系统施加的限制内，如果任意的Unicode字符串可以用作文件名则返回`True`，否则返回`False`

#### 判断 多文件是否相同

##### 01 判断 目录或文件是否相同

> `os.path.samefile(path1, path2)`

##### 02 判断 文件指针fp1和fp2是否指向同一文件

> `os.path.sameopenfile(fp1, fp2)`

##### 03 判断 stat tuple stat1和stat2是否指向同一个文件

> `os.path.samestat(stat1, stat2)`


### C：获取路径指向的信息

#### 获取 访问时间

> `os.path.getatime(路径)`

#### 获取 修改时间

> `os.path.getmtime(路径)`

#### 获取 改变时间

> `os.path.getctime(路径)`
>
> - 访问时间与修改时间中有一个改变，`ctime`就会随之改变，它反映了用户**接触**文件的时间，这个接触的概念，包括了访问和修改

#### 获取 文件大小

> `os.path.getsize(路径)`
>
> - 如果**文件不存在会报错**。如果不想让其报错，需要在调用这个方法前，先调用`os.path.exists`判断其是否存在

### D：路径处理

#### 路径依序串联

> `os.path.join(路径)`
>
> 大致相当于把路径用`+`号相连，可以让你少写一些`/`

#### 替换`~`符号

> `os.path.expanduser(路径)`
>
> 把路径中包含的"~"和"~user"转换成用户目录

#### 替换`${变量}`为环境变量中的值

> `os.path.expandvars(路径)`
>
> 根据环境变量的值替换路径中包含的"$name"和"${name}"

#### 规范 路径大小写

> `os.path.normcase(路径)`
>
> - **这个方法是以`Unix`系统族为标准的，所以在`Unix`和`Mac OS X`上，返回路径不变；**
>
> - 在不区分大小写的文件系统上，它将路径转换为小写；
>
> - **在`Windows`上，它还将正斜杠转换为反斜杠**（`python`不认为`Windows`是标准呢~）

#### 规范 路径符号使用

> `os.path.normpath(路径)`
>
> - 折叠冗余，规范上一级引用符号`..`的使用。例如：
>
>   `A//B`、`A/B/`、`A/./B`、`A/C/../B`这些都会被规范化为`A/B`
>
> - **在`Windows`上，它还将正斜杠转换为反斜杠**
>
>   ​	题外话：其实这个很有用，因为像`A/B/`在获取`basename`时，返回的会是空字符串，所以可以在`os.path.basename`之前先`os.path.normpath`一下


#### 分离`dirname`和`basename`

> `os.path.split(路径)`
>
> 先如下例子：
>
> ```python
> >>> import os.path as path
> >>> path.split('C:/soft/python/test.py')
> ('C:/soft/python', 'test.py')
> >>> path.split('C:/soft/python/')
> ('C:/soft/python', '')
> ```
>
> - 它是以路径最后一个`/`为分隔，分隔`dirname`与`basename`
> - 需要注意的是，它和`os.path.basename`存在相同的问题，即以`/`结尾会导致`basename`为空字符串

#### 分离 盘符 和 剩余路径

> `os.path.split(路径)`
>
> ```python
> # Linux上
> >> import os.path as path
> >> path.splitdrive("/tmp/test.py")
> ('', '/tmp/test.py')
> 
> # Windows上，若含有驱动器
> >> import os.path as path
> >> path.splitdrive("E:\test.py")
> ('E:', '\test.py')
> 
> # Windows上，共享文件
> >> import os.path as path
> >> path.splitdrive("//host/computer/dir")
> ("//host/computer", "/dir")
> ```
>
> - 在不使用盘符的系统上（例如Linux），盘符名将始终为空字符串
>
> - 盘符包含双引号，而其余路径开头会包含斜杠或反斜杠
>
> - 如果路径包含UNC路径，则驱动器将包含主机名和共享，但不包括第四个分隔符
>

#### 分离 文件拓展名

> `os.path.splitext(路径)`
>
> 先举如下例子：
>
> ```python
> >>> import os.path as path
> >>> path_01='/tmp/example.tar.gar'
> >>> path_02='/tmp/example'
> >>> path.splitext(path_01)
> ('/tmp/example.tar', '.gar')
> >>> path.splitext(path_02)
> ('/tmp/example', '')
> ```
>
> 由此可见：
>
> - 该方法的返回值为元组
> - 该方法并没舍弃被分离的后缀
> - 值得吐槽的是，它**只分离了最后一个`.`之后的后缀**
> - 它用处最多的地方是判断文件类型（例如是`.exe`还是`.txt`？）










