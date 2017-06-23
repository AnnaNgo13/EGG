import re
import logging

logging.basicConfig(filename='egg.log', level=logging.DEBUG,format='%(asctime)s %(message)s')

def graph_parser(schema):

	egg=dict() #### global variable : keys are graph nodes and edges id
	
	graph_elements=dict()
	
	with open(schema+'-graph.txt','r') as f:
		for line in f.readlines():
			match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
			if match:
				# parse edges
				if match.group(4) in graph_elements: 
	  				graph_elements[match.group(4)].add(match.group(5))
	  				egg[match.group(5)]=dict()
	  				egg[match.group(5)].update({"out":match.group(3)})
	  				egg[match.group(5)].update({"in":match.group(7)})
				else:
	 				graph_elements[match.group(4)]={match.group(5)}
	 				egg[match.group(5)]=dict()
	 				egg[match.group(5)].update({"out":match.group(3)})
	  				egg[match.group(5)].update({"in":match.group(7)})
	 			# parse source nodes 
	 			if match.group(2) in graph_elements: 
	  				graph_elements[match.group(2)].add(match.group(3))
	  				egg[match.group(3)]=dict()
				else:
	 				graph_elements[match.group(2)]={match.group(3)}
	 				egg[match.group(3)]=dict()
	 			# parse object nodes
	 			if match.group(6) in graph_elements: 
	  				graph_elements[match.group(6)].add(match.group(7))
	  				egg[match.group(7)]=dict()
				else:
	 				graph_elements[match.group(6)]={match.group(7)}
	 				egg[match.group(7)]=dict()

	

	return (egg,graph_elements)