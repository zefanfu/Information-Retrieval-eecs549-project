from flask import *

from extensions import *

from config import *

import hashlib

import os,sys
import subprocess
import tempfile
from sphinxapi import *
import json
import sphinxsearch
museum = Blueprint('museum', __name__, template_folder='templates')
@museum.route('/museum', methods=['GET', 'POST'])
def museum_route():
	query = request.args.get('query')
	search = True
	if query == None:
		query = ""
		search = False
	no_museum = False
	museum = list()
	single = False

	with tempfile.TemporaryFile() as tempf:
		cmd = ['search']
		cmd.append(query)
		proc = subprocess.Popen(cmd, stdout=tempf)
		proc.wait()
		tempf.seek(0)
		output = tempf.read()

	client = SphinxClient()
	client.SetServer('localhost', 9312)
	client.SetSortMode(SPH_SORT_ATTR_DESC, 'Museum_Type')
	client.SetMatchMode(SPH_MATCH_ALL)
	client.SetLimits(0, 50)
	obtained = client.Query(query)
	getlist = obtained['matches']
	f = open('output1.txt', 'w')
	for i in getlist:
		r = json.dumps(i)
		f.write(r)
		f.write('\n')
	f.close()
	f = open("output1.txt")
	data = list()
	for line in f:
		data.append(line)

	f.close()
	for i in range(len(data)):
		data[i] = data[i].replace("\"", "")
		data[i] = data[i].replace("\'", "")
		data[i] = data[i].replace("\\", "")

	ff = open("out2.txt", "w")
	for tmp in data:
		ff.write(tmp)
		ff.write("\n")

	ff.close()
	if len(getlist) <= 5:
		museum = getlist
	else:
		for i in range(5):
			museum.append(getlist[i])

	if (len(museum) == 0):
		no_museum = True
	options = {
		'host': config.env['host'],
		'port': config.env['port'],
		'query': query,
		'single': single,
		'search': search,
		'no_museum':no_museum,
		'museum': museum
	}
	return render_template("museum.html", **options)

@museum.route('/museum/single', methods=['GET', 'POST'])
def museum_single_route():
	singleinfo = request.form.get('singleinfo')
	single = True
	options = {
		'host': config.env['host'],
		'port': config.env['port'],
		'single': single,
		'singleinfo': singleinfo
	}
	return render_template("museum.html", **options)
