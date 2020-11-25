
import pafy 
  
url = "https://www.youtube.com/watch?v=iGxFLjqhkSA&list=PLwygboCFkeeA2w1fzJm44swdG-NnyB6ip&index=134&t=0s"
video = pafy.new(url) 
  
streams = video.streams 
for i in streams: 
    print(i) 
      
# get best resolution regardless of format 
best = video.getbest() 
  
print(best.resolution, best.extension) 
  
# Download the video 
best.download() 

