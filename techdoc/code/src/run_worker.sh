#!/bin/sh
# this is run under /lmt/backend
cd ..
mkdir -p tmp_media/$1
wget -P tmp_media/$1 mite/result/$1/cfg.gls
cd worker
./run_glass -t 4 ../tmp_media/$1/cfg.gls
cd ..
# upload files to server
scp tmp_media/$1/* lmt@mite:/srv/lmt/tmp_media/$1/
rm tmp_media/$1/*