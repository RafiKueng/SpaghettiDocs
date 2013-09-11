# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:01:42 2013

@author: RafiK
"""

import os

import pygments as pyg
from pygments import lexers
from pygments import formatters


inppath = os.path.abspath('../code/src/')
outpath = os.path.abspath('../code')

outstyle = '__style.tex'

# http://pygments.org/docs/formatters/
latexFormat = pyg.formatters.LatexFormatter(
  linenos=True,
  commandprefix='PYG',
  mathescape=True
  )


for root, dirs, files in os.walk(inppath):
  for fname in files:
    subdir = root[len(inppath)+1:]

    print '> converting:', subdir, fname, 
    with open(os.path.join(root,fname)) as f:
      code = f.read()
  
    lexer = pyg.lexers.get_lexer_for_filename(fname)
    
    name = (subdir+'__' if subdir else '') + fname + '.tex'
    p=os.path.join(outpath, name)
    with open(p, 'w') as outfile:
      outstr = pyg.highlight(code, lexer, latexFormat, outfile)
      
    print '>', name
    
print "creating stylefile",
with open(os.path.join(outpath, outstyle), 'w') as f:
  f.write(latexFormat.get_style_defs())