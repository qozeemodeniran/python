try:
    f = open("info.txt")
    try:
        f.write("Qozeem Odeniran")
    except:
        print("Something went wrong when opening the file")
    finally:
        f.close()
except:
    print("Something went wrong when trying to open the file")