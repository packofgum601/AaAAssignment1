import os

# Create datafiles directory if it doesn't exist
if not os.path.exists("datafiles"):
    os.mkdir("datafiles")
    


with open("sampleData200k.txt", "r") as f:
    data = f.read()
    
    words = data.split("\n")
    
    data500 = words[:500]
    data10k = words[:10000]
    data50k = words[:50000]
    data100k = words[:100000]
    
    with open("datafiles/sampleData500.txt", "w") as f:
        for word in data500:
            f.write(word + " \n")
            
    with open("datafiles/sampleData10k.txt", "w") as f:
        for word in data10k:
            f.write(word + " \n")
            
    with open("datafiles/sampleData50k.txt", "w") as f:
        for word in data50k:
            f.write(word + " \n")
    