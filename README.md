# laghing
A python side project.

## packages needed:
1. pip
2. distribute
3. nose
4. virtualenv

## NOTES
1. `python setup.py install` 打包项目并安装到本机
2. `nosetests` 即可执行测试
3. 

```
  'packages': ['bin', 'NAME'], # 项目需要用到的子模块
  'scripts': ['./bin/hello'], # 指定可执行文件以便安装后调用
```