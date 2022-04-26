import requests, zipfile, glob, os

BASE_URL = "https://cims.coastal.louisiana.gov/RequestedDownloads/ZippedFiles/"
data_types = [
  "Full_Continuous_Hydrographic", 
  "Full_Discrete_Hydrographic", 
  "Full_Marsh_Vegetation", 
  "Full_Forest_Vegetation", 
  "Full_Surface_Elevation", 
  "Full_Soil_Properties", 
  "Full_Accretion", 
  "Full_Biomass"
]

for data_type in data_types:
  url = BASE_URL + data_type + ".zip"
  print("Downloading file from " + url)
  response = requests.get(url)
  with open(data_type + ".zip", "wb") as output_file:
    output_file.write(response.content)
  with zipfile.ZipFile(data_type + ".zip","r") as zip_ref:
    zip_ref.extractall("./data")
  # delete temporary files created during download and unzipping
  for file in glob.glob(data_type + "*"):
    os.remove(file)
  print("Finished downloading file from " + url)