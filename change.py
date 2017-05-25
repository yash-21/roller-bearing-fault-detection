with open("output_id31.txt","rb") as infile:
	with open("output_id3f.txt","wb") as outfile:
		data = infile.read()
                data = data.replace(",", "")
		data = data.replace("[", "")
		data = data.replace("]", "")
                outfile.write(data)

