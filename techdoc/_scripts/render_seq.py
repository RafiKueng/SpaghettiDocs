# -*- coding: utf-8 -*-
"""
renders all sequence diagrams

Created on Thu Sep 12 14:50:31 2013

@author: RafiK
"""

import os
import subprocess as sp

inppath = os.path.abspath('../seq/src/')
outpath = os.path.abspath('../seq')
#inppath = r'..\seq\src'
#outpath = r'..\seq'


exe_path = r'D:/devtools/sequenzdiagram/'
#exe_path = r'.'
exe_cmd = 'sdedit-4.01.exe'
exe_args = '-t pdf -f A4 -r Landscape --threaded=false' # doesn't work

# there is also linux/max (java) version..
#exe_cmd = 'java -jar sdedit-4.01.jar'
#exe_cmd = 'sdedit.sh'


exep = os.path.join(os.path.abspath(exe_path), exe_cmd)
#args = ' -o %(out)s ' + exe_args + ' %(inp)s'
args = ' -o %(out)s %(inp)s'

def cmd(inp, out):
#  sp.call('pwd')
#  sp.call([exep, args % {'inp':inp, 'out':out}], shell=True)
#  print exep + ' ' + args % {'inp':inp, 'out':out}
  sp.call(exep + ' ' + args % {'inp':inp, 'out':out})
  



for root, dirs, files in os.walk(inppath):
  for fname in files:
    if fname.endswith('.sdx') or fname.endswith('.sd'):
      name, ext = os.path.splitext(fname)
      outname = name + '.pdf'
      inpf = os.path.join(inppath, fname)
      outf = os.path.join(outpath, outname)
      #inpf = inppath +'\\'+ fname
      #outf = outpath +'\\'+ outname
      print '> convert:', fname,
      cmd(inpf, outf)
      print '>>', outname, ' STARTED'