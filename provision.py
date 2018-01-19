#!/usr/bin/python

from ecsclient.client import Client

import sys
import os
import time
import subprocess
import re
import json
import argparse

STORAGE_POOL = "bosh"
VIRTUAL_DATA_CENTER = "bosh_vdc"
REPLICATION_GROUP = "bosh_rep_grp"
NAMESPACE = "bosh-namespace"

parser = argparse.ArgumentParser(description="provision ECS cluster")
parser.add_argument("scriptname", nargs=1)
parser.add_argument("nodes", nargs=3)
parser.add_argument("ecs_mgt", nargs=1)
parser.add_argument("-v", action="store_true", default=False, dest="verbose")
parser.add_argument("-u", action="store", default="root", dest="user")
parser.add_argument("-p", action="store", default="ChangeMe", dest="pwd")

vals = parser.parse_args(sys.argv)

ALL_NODES = vals.nodes
NODE0 = vals.nodes[0]
NODE1 = vals.nodes[1]
NODE2 = vals.nodes[2]
ECS_MGT = vals.ecs_mgt[0]
VERBOSE = vals.verbose
USERNAME = vals.user
PASSWORD = vals.pwd

if VERBOSE:
    print "--- Parsed Configuration ---"
    print "Username: %s" % USERNAME
    print "Password: %s" % PASSWORD
    print "ECS API endpoint: %s" % ECS_MGT
    print "ECS Node 0: %s" % NODE0
    print "ECS Node 1: %s" % NODE1
    print "ECS Node 2: %s" % NODE2
    print "ECS Storage Pool: %s" % STORAGE_POOL
    print "ECS Virtual Data Center: %s" % VIRTUAL_DATA_CENTER
    print "ECS Replication Group: %s" % REPLICATION_GROUP
    print "ECS Namespace: %s" % NAMESPACE


client = Client('3', username='root', password='ChangeMe',
                token_endpoint='https://'+ ECS_MGT +':4443/login',
                ecs_endpoint='https://'+ ECS_MGT + ':4443')

with open ("./license.lic", "r") as myfile:
    liscense=myfile.read()

response = client.licensing.add_license(liscense)

if VERBOSE:
    print "--- Add License Response ---"
    print response
    print "----------------------------"


response = client.storage_pool.create(STORAGE_POOL)

if VERBOSE:
    print "--- create storage pool Response---"
    print response
    print "----------------------------"


