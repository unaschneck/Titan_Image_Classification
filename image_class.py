########################################################################################################################################
# Pre-processing and Image Classifer
# Objective:
# Date Started: December 2020
########################################################################################################################################
from datetime import datetime
import os

labels = ["craters", "plains", "labyrinth", "hummocky", "lakes", "dunes"] # terrian types

def preProcessing(image_directory, to_print):
	# run pre-processing on image file
	if to_print: print("\ntotal image files in '{0}' = {1}".format(image_directory, len(os.listdir(image_directory))))

#### IMAGE TERRAIN CLASSIFERS: MORPHOLOGICAL and ALBEDO
#### TYPES: Craters, Plains, Labyrinth, Hummocky Terrain, Lakes, Dunes

## MORPHOLOGICAL CLASSIFER
def morphologicalClassifer(image_directory, to_print):
	###############################################
	## Based on the physical features
	#
	# Note: Preliminary features for classification
	# Craters: Round
	# Plains: Lacks topographic relief
	# Labyrinth: Locally elevated
	# Hummocky: Higher topographically than surrounding terrain
	# Lakes: Typically has raised rims and steep sides
	# Dunes: Long, narrow features with regular spacing
	#
	###############################################
	if to_print: print("\nMorphological Classifer")
	if to_print: print("total image files in '{0}' = {1}".format(image_directory, len(os.listdir(image_directory))))

## ALBEDO CLASSIER
def albedoClassifer(image_directory, to_print):
	###############################################
	## Based on the light or darkness of a region
	#
	# Note: Peleminary features for classification
	# Craters: Low microwave Emissivity in ejecta blanket
	# Plains: Dark in SAR, High Emissivity in RADAR
	# Labyrinth: High emissivity
	# Hummocky: Bright in SAR, Low Emissivity in RADAR, High Scatter in RADAR
	# Lakes: Dark in SAR
	# Dunes: Dark in SAR, High Emissivity in RADAR
	#
	###############################################
	if to_print: print("\nAlbedo Classifer")
	if to_print: print("total image files in '{0}' = {1}".format(image_directory, len(os.listdir(image_directory))))

if __name__ == '__main__':
	start_time = datetime.now()

	import argparse
	# file run: python image_class.py -I image_file.jpg -P True
	parser = argparse.ArgumentParser(description="flag format given as: -I <image_file.jpg> -P <True/False>")
	parser.add_argument('-I', '-image-directory', help="file of images")
	parser.add_argument('-P', '-print-sentences', choices=("True", "False"), default="False", help="print sentences")
	args = parser.parse_args()
	
	# get image file to classify
	if args.I is None:
		print("\nERROR: Include valid image directory\n")
		exit()
	else:
		given_image_directory = args.I
	
	# argument to print details for the command prompt
	to_print = args.P
	to_print = True if args.P == 'True' else False # cast as true/false from input string

	# Reviewing and cleaning images (as needed)
	preProcessing(given_image_directory, to_print)

	# Morphological Classifer (TODO)
	morphologicalClassifer(given_image_directory, to_print)

	# Albedo Classifer (TODO)
	albedoClassifer(given_image_directory, to_print)

	print("\nran for for {0}\n".format(datetime.now() - start_time))
