###############################
#
#
#
#
#
import numpy as np
import matplotlib.pyplot as plt
import argparse



parser = argparse.ArgumentParser(description='choose the file to plot.')

parser.add_argument('file', metavar='file', type=str, nargs=1,
                   help='the file to plot')

args = parser.parse_args()

file = args.file[0]

file_list = file.split("-")

x=list()
y=list()

with open (file+'.txt','r') as f:

	for line  in f.readlines():

		x.append(line.split(";")[0])
		y.append(line.split(";")[1])

plt.plot(x,y,"bo-")

if file_list[2] == "interval" :
	plt.xlabel("# of graph nodes", fontsize=14, color='black')
else:
	plt.xlabel("# of graph snapshots", fontsize=14, color='black')

		
plt.ylabel('Time in seconds', fontsize=14, color='black')
plt.xscale("log", nonposx='clip')
plt.yscale("log", nonposy='clip')
plt.grid()
if file_list[2] == "interval" :
	plt.title(file_list[5]+" use case: "+"# of graph snapshots"+" set to "+file_list[4])
else :
	plt.title(file_list[5]+" use case: "+"# of graph nodes"+" set to "+file_list[4])

plt.savefig(file_list[2]+"_"+file_list[5]+".png")
plt.clf()





