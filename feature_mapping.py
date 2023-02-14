from flask import Flask, jsonify, request
import pickle
import shap
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def feature_map(top_3_features):
	categories = {'diet':0, 'wellness':0, 'exercise':0, 'community':0, 'healthliteracy':0, 'other':0}

	diet = ["C419.0", "C3030.0", "M14.0", "C2903.0", "otherdisorder", "anxiety", "mooddisorder", "dbp3rd"]
	exercise = ["C419.0", "C3030.0", "M14.0", "C2903.0", "otherdisorder", "anxiety", "mooddisorder"]
	wellness = ["C4527.0"]
	community = ["C3725.0"]
	healthliteracy = ["C2398.0", "edvisitcount"]

	for feature in top_3_features:
		if feature in diet:
			categories['diet'] +=1

		elif feature in exercise:
			categories['exercise']+=1

		elif feature in wellness:
			categories['wellness'] +=1

		elif feature in community:
			categories['community'] +=1

		elif feature in healthliteracy:
			categories['healthliteracy'] +=1

		else:
			categories['other'] +=1

	content = max(categories, key = categories.get)
	return content