# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 14:30:25 2023

@author: Amar Doshi
"""


def replaceFileExt(fileName: str, newExtension: str) -> str:
    fileName = fileName.strip()
    newExtension = newExtension.strip()

    if (i := fileName.rfind('.')) > -1:
        fileName = fileName[:i]

    if not newExtension.startswith('.'):
        newExtension = f'.{newExtension}'

    return f'{fileName}{newExtension}'


if __name__ == '__main__':

    f = ('', '.', '.ext', 'filename', 'filename.', 'filename.ext', 'file.name.ext')
    e = ('', '.', 'txt', '.txt', 'txt.csv', '.txt.csv')

    for i in f:
        print()

        for j in e:
            print(replaceFileExt(i, j))
