# Python 卸载包 方法汇总

## 卸载 pip 安装的包

```bash
pip uninstall <package>
```

## 卸载 easy_install 安装的包

```bash
easy_install -m <package>
```

## 卸载通过 setup.py 安装的包

```bash
# 安装包时需要记录日志
python setup.py install --record installation.log

# 卸载的时候，使用日志文件
cat installation.log | xargs rm -rf
```

