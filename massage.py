#!/usr/bin/python

import json

infile = "core.kr.json"
outfile = "outfile"

with open(infile,'r') as inf:
    data = inf.read()

pdata = json.loads(data)

start = 0
end = len(pdata)

outf = open(outfile,'w')

for i in range(start, end):

    if ( pdata[i].has_key("flavor") ):
        mystring = '"%s","%s","%s","%s"\n' %(pdata[i]["code"],pdata[i]["title"],pdata[i]["text"],pdata[i]["flavor"])
    else:
        mystring = '"%s","%s","%s"\n' %(pdata[i]["code"],pdata[i]["title"],pdata[i]["text"])

    outf.write(mystring.encode('utf-8'))

outf.close()
inf.close()
