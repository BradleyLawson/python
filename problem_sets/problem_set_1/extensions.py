def main():
    fileName = lastWord(input("File Name: ").strip().lower())
    print(mediaType(fileName))

def lastWord(str):
    if "." not in str:
        return str
    else:
        return str.split(".")[-1]

def mediaType(file):
    match file:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"  
    
main()