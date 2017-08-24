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
restaurant = Blueprint('restaurant', __name__, template_folder='templates')
@restaurant.route('/restaurant', methods=['GET', 'POST'])
def restaurant_route():
    query = request.args.get('query')
    single = False
    search = True
    if query == None:
        query = ""
        search = False
    restaurant = list()
    no_rest = False

    typename = request.args.get('typename')
    if typename == None:
        typename = "general"
    if query == None:
        query = ""
    restaurant = list()
    museum = list()
    query = "chinese"
    print(1)
    ##########################################
    #####################################################
    with tempfile.TemporaryFile() as tempf:
        cmd = ['search']
        cmd.append(query)
        proc = subprocess.Popen(cmd, stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = tempf.read()

    getlist = list()
    client = SphinxClient()
    client.SetServer('localhost', 9312)
    client.SetSortMode(SPH_SORT_ATTR_DESC, 'stars')
    client.SetMatchMode(SPH_MATCH_ALL)
    client.SetLimits(0, 50)
    obtained = client.Query(query)
    print(obtained)
    getlist = obtained['matches']
    print(2)
    f = open('output.txt', 'w')
    for i in getlist:
        r = json.dumps(i)
        f.write(r)
        f.write('\n')
    f.close()
    f = open("output.txt")
    data = list()
    for line in f:
        data.append(line)

    for i in range(len(data)):
        data[i] = data[i].replace("\"", "")
        data[i] = data[i].replace("\'", "")
        data[i] = data[i].replace("\\", "")

    ff = open("out1.txt", "w")
    for tmp in data:
        ff.write(tmp)
        ff.write("\n")

    ff.close()
    res = list()
    # Key: Alcohol, Val: unknow, others
    # Key:
    for tmp in data:
        tmp_dict = dict()
        if "Alcohol" in tmp:
            mess = tmp.split("Alcohol: ", 1)[1]
            mess = mess.split(";", 1)[0]
            tmp_dict["Alcohol"] = mess

        else:
            tmp_dict["Alcohol"] = ""

        Ambience = False
        Ambience_list = list()
        if "Ambience" in tmp:
            mess = tmp.split("Ambience: {", 1)[1]
            mess = mess.split("}", 1)[0]
            if "True" in mess:
                Ambience = True
                mess = mess.split("; ")
                for sub_mess in mess:
                    sub_mess = sub_mess.split(": ")
                    if sub_mess[1] == "True":
                        Ambience_list.append(sub_mess[0])

        tmp_dict["Ambience"] = Ambience
        tmp_dict["Ambience_list"] = Ambience_list

        GoodForMeal = False
        GoodForMeal_list = list()
        if "GoodForMeal" in tmp:
            mess = tmp.split("GoodForMeal: {", 1)[1]
            mess = mess.split("}", 1)[0]
            if "True" in mess:
                GoodForMeal = True
                mess = mess.split("; ")
                for sub_mess in mess:
                    sub_mess = sub_mess.split(": ")
                    if sub_mess[1] == "True":
                        GoodForMeal_list.append(sub_mess[0])

        tmp_dict["GoodForMeal"] = GoodForMeal
        tmp_dict["GoodForMeal_list"] = GoodForMeal_list

        Caters = False
        if "Caters" in tmp:
            Caters = True

        tmp_dict["Caters"] = Caters

        city = ""
        if "city" in tmp:
            mess = tmp.split("city: ", 1)[1]
            city = mess.split(",", 1)[0]

        tmp_dict["city"] = city

        name = ""
        if "name" in tmp:
            mess = tmp.split("name: ", 1)[1]
            name = mess.split(",", 1)[0]

        tmp_dict["name"] = name

        categories = list()
        if "categories" in tmp:
            mess = tmp.split("categories: [", 1)[1]
            mess = mess.split("]", 1)[0]
            categories = mess.split("; ")

        tmp_dict["categories"] = categories

        BusinessParking = False
        BusinessParking_list = list()
        if "BusinessParking" in tmp:
            mess = tmp.split("BusinessParking: {", 1)[1]
            mess = mess.split("}", 1)[0]
            if "True" in mess:
                BusinessParking = True
                mess = mess.split("; ")
                for sub_mess in mess:
                    sub_mess = sub_mess.split(": ")
                    if sub_mess[1] == "True":
                        BusinessParking_list.append(sub_mess[0])

        tmp_dict["BusinessParking"] = BusinessParking
        tmp_dict["BusinessParking_list"] = BusinessParking_list

        longitude = ""
        if "longitude" in tmp:
            mess = tmp.split("longitude: ", 1)[1]
            longitude = mess.split(",", 1)[0]

        tmp_dict["longitude"] = longitude

        latitude = ""
        if "latitude" in tmp:
            mess = tmp.split("latitude: ", 1)[1]
            latitude = mess.split(",", 1)[0]

        tmp_dict["latitude"] = latitude

        address = ""
        if "address" in tmp:
            mess = tmp.split("address: ", 1)[1]
            address = mess.split(",", 1)[0]

        tmp_dict["address"] = address
        stars = ""
        if "stars" in tmp:
            mess = tmp.split("stars: ", 1)[1]
            stars = mess.split(",", 1)[0]

        tmp_dict["stars"] = stars
        if "type" in tmp:
            res.append(tmp_dict)

    if len(res) <= 5:
        restaurant = res
    else:
        for i in range(5):
            restaurant.append(res[i])

    print("HERE!!!!!!!!!!!!!!!!!!!!!!!!")
    print(restaurant)



    if (len(restaurant) == 0):
        no_rest = True

    options = {
        'host': config.env['host'],
        'port': config.env['port'],
        'search': search,
        'query': query,
        'restaurant': restaurant,
        'no_rest': no_rest,
        'single': single
    }
    return render_template("restaurant.html", **options)

@restaurant.route('/restaurant/single', methods=['GET', 'POST'])
def restaurant_single_route():
    singleinfo = request.form.get('singleinfo')
    single = True
    options = {
        'host': config.env['host'],
        'port': config.env['port'],
        'single': single,
        'singleinfo': singleinfo
    }
    return render_template("restaurant.html", **options)
