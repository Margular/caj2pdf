#!/usr/bin/env python3
import os

from cajparser import CAJParser

if __name__ == "__main__":
    for filepath in os.listdir():
        filename, fileext = os.path.splitext(filepath)
        if fileext != '.caj':
            continue
        try:
            caj = CAJParser(filepath)
            caj.convert(filename + '.pdf')
        except Exception:
            open('一键转换caj到pdf失败的文件清单.txt', 'a').write(filepath + '\n')
