import os
import math
import re
import json
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo # enables Flask to connect to MongoDB Atlas
from bson.objectid import ObjectId 
from werkzeug.utils import secure_filename

"""
MongoDB represents JSON documents in binary-encoded format called BSON behind the scenes.
BSON extends the JSON model to provide additional data types, ordered fields, and to be
efficient for encoding and decoding within different languages.
"""

app = Flask(__name__)

