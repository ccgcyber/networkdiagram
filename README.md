# networkdiagram
Create a visual network diagram from traceroutes

#How To
- Open the hosts.txt file and add ips you want to trace route. 
- Run one of the python files.
- View the html page in browser.

#What it does.
The python file opens the hosts.txt file and gets the ips. It then runs a traceroute and builds the routes.txt file from it. It then traverses the routes.txt file and creates a flare.json file from the info. 
When you open up the web file (Daigram.html etc) it uses d3.js to create the graphs from this data. The nodes are clickable
