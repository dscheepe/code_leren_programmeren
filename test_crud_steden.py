from crud_steden import maak_data_string

#get data string from list(maak_data_string() function of crud_steden)
ds_steden = maak_data_string()
#data string naar een list.
steden = ds_steden.split(",")
print(steden)
