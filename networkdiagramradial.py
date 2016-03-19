#Author: Jacques Coetzee
#Date 18 MArch 2015
#Comment: Built with python 3
#How to:
#Create a file called hosts.txt.
#In this file add a single ip per line that you want to have on your diagram
#eg:

#192.168.0.1
#192.168.2.1
#google.com
#absa.co.za

import subprocess

f = open('hosts.txt', 'rb')
records = f.readlines()
f.close()


f = open('routes.txt','w')
for ix,ip in enumerate(records):
    ip = str(ip)
    batcmd="tracert -d %s" % ip
    result = subprocess.check_output(batcmd, shell=True)
    print 'Traceroute complete %s' % ip
    result = result.split('\n')
    oldip = '127.0.0.1'
    for ix, line in enumerate(result):
        line = line.strip()
        if (line != '') and ('Trac' not in line) and ('hops' not in line):
            if 'out.' in line:
                oldip = oldip + ',*'
            else:
                oldip = oldip + ',' + line.split(' ')[-1]
    f.write( oldip + '\n')
            
            
f.close()

f=open('routes.txt', 'rb')
routes=f.readlines()
f.close()

flare = {}

for route in routes:
     
    hops = str(route).strip().split(',')
    tmp=flare
    for ix, hop in enumerate(hops):
        
        tst = str(hop).strip()
        
        if ix == 0:
            if not hop in tmp:
                tmp[hop] = {}
            tmp = tmp[hop];
        else:
            if not hop in tmp:
                tmp[hop] = {}
            tmp = tmp[hop];
            

json = ''


def recurse(d, ident):
  global json
  if len(d) > 0:
    for ix,k in enumerate(d):
      spaces = ' '*ident
      json = json + spaces + '{'
      json = json + spaces + '"name": "%s", "size": 3041,' % k
      json = json + spaces + '"children": ['
      ident = ident + 2
      recurse(d[k], ident)
      ident = ident - 2
      json = json +spaces + ']'
      if ix+1 != len(d):
          
          json = json + spaces  + '},'
      else:
          json = json + spaces + '}'
  #else:
  #  print('*'*ident,d)


recurse(flare,2)

f=open('flare.json', 'wb')
f.write(json)
f.close()
import os
os.system('index.html')


