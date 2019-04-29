# change the MD5 [![The MIT License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](http://opensource.org/licenses/MIT) [![PyPI](https://img.shields.io/pypi/v/ctmd5.svg?style=flat-square)](https://pypi.python.org/pypi/ctmd5)

有时候在使用某网盘的时候总会遇到文件无法上传或者是上传后无法分享的情况，所以抽了个时间写了个改变文件 MD5 值的小工具，目前只能算是基本能用吧，后续再继续完善。

## 安装
``` shell
$ pip3 install ctmd5
```

## 使用
``` shell
$ ctmd5 -h
usage: ctmd5.py [-h] [-s] [-v] FILE

a cli tool used to change the MD5 of files

positional arguments:
  FILE           the file you want to change md5

optional arguments:
  -h, --help     show this help message and exit
  -s, --show     show the md5 value
  -v, --version  show program's version number and exit
```

## 示例

运行

``` shell
$ ctmd5 -s The.Big.Bang.Theory.mp4
before: 23aefe6872325590956548dec285849f
The md5 value has been changed.
after: 447e1bb20de228dcdead50db56415b7c
```

## LICENSE

MIT [@shkey](https://github.com/shkey)
