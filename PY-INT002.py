import os
import pathlib
import shutil

fileFormat = {
	"Picture": [".png", ".jpg", ".jpeg", ".bpg",],

	"Video": [".mp4", ".mkv", ".vob", 
	          ".mov", ".avi",],

	"Document": [".pdf", ".doc", ".docx", 
	          ".txt", ".dox", ".xps", ".ppt", 
	          ".pptx", ".xls", ".xlsx", ".pages",],

	"Audio": [".mp4", ".m4a", ".m4b", 
	          ".aac", ".raw",]

}

fileTypes = list(fileFormat.keys())
fileFormat = list(fileFormat.values())

print(fileFormat)
print(fileTypes)

for file in os.scandir():
	fileName = pathlib.Path(file)
	fileFormatType = fileName.suffix.lower()

	src = str(fileName)
	dest = "Other"
	if fileFormatType == "":
		print(f" {src} there is no file ")
	else:
		for formats in fileFormat:
			folder = fileTypes[fileFormat.index(formats)]

			if os.path.isdir(folder) == False:
			   os.mkdir(folder)
			   dest = folder
		else:
			if os.path.isdir("other") == False:
				os.mkdir("other")

print(src , "move to", dest, "!")
shutil.move(src,dest)


print("File organizer start")
input("\n press enter to EXIT")