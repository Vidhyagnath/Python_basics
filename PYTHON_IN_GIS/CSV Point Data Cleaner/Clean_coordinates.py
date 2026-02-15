import pandas as pd
df=pd.read_csv("Project2/Coordinates.csv")
print(df)
df=df.dropna()
print("\n After removing empty rows:")
print(df)
def check_latitude(lat):
    if lat>=-90 and lat<= 90:
        return True
    else:
        return False
def check_longitude(lon):
    if lon>=-180 and lon<= 180:
        return True
    else:
        return False
df=df[df.apply(lambda row: check_latitude(row["Latitude"]) and check_longitude(row["Longitude"]),axis=1)]
print("\n \n After checking the Coordinates")
print(df)
df=df.drop_duplicates(subset=["Latitude","Longitude"])
print("\n \n After removing duplicates")
print(df)
df.to_csv("Cleaned_Coordinates.csv",index=False)
print("\n✅ Clean file saved as cleaned_coordinates.csv")
