# export services object to csv files ready for database insertion
def export_csvs(services_filename, images_filename, services):
    services_file = open(services_filename, "w")
    images_file = open(images_filename, "w")

    services_file.write("service_id,latitude,longitude,title,type\n")
    images_file.write("service_id,image_url\n")

    for i in range(len(services)):
        service_id = str(services[i]["id"])
        latitude = str(services[i]["latitude"])
        longitude = str(services[i]["longitude"])
        title = services[i]["title"]
        type = services[i]["type"]

        services_file.write(service_id + "," + latitude + "," + longitude + "," + title + "," + type + "\n")
        
        for image_url in services[i]["images"]:
            images_file.write(service_id + "," + image_url + "\n")

    services_file.close()
    images_file.close()