videoer = [
'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
'https://www.youtube.com/watch?v=cpPG0bKHYKc',
'https://www.youtube.com/watch?v=hFhiV5X5QM4',
'https://www.youtube.com/watch?v=6r1DFGpBzrc',
'https://www.youtube.com/watch?v=Ow3CcOGNIss',
'https://www.youtube.com/watch?v=z9Uz1icjwrM']

id_tag = "v="

videoer_ny = []

for url in videoer:
    id = url[int(url.find(id_tag)+len(id_tag)) : len(url)]
    videoer_ny.append("Youtu.be/" + id)
    
for url in videoer_ny:
    print(url)