def main():
    parser = argparse.ArgumentParser(description='Loate Food Truck')

    parser.add_argument("lat")
    parser.add_argument("long")
    parser.add_argument("radius")
    args = parser.parse_args()

    db = get_db()   #connect to database
    lat = float(args.lat)  # degrees
    longit = float(args.long)  # degrees
    radius = float(args.radius)  # miles

    latMin, latMax = getLatMinMax(lat, radius)
    lngMin, lngMax = getLongMinMax(longit, lat, radius)
    lst = getTrucks(db,lat, longit, latMin, latMax, lngMin, lngMax, radius)

    # output the 5 "closest food trucks"
    print("The closest food trucks to your location are:")
    for doc in lst:
        pprint(doc)

if __name__ == '__main__':
   main()
