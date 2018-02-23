import os, sys

a=os.path.dirname(sys.argv[0])
mp3=[]
link=os.path.join(a,"playlistcreator.txt")
text=open(link,'r')
string=str(text.read())
text.close()


for name in os.listdir(string):
    path=os.path.join(string,name)
    
    if os.path.isfile(path):
        splitting=os.path.splitext(name)
        
        if splitting[1]==".mp3" or splitting[1]==".MP3":
            mp3.append(splitting[0])
            


if not mp3:
    print "There is no mp3 song in the folder"
else:
    filename=os.path.join(string,"playlist MP3")
    file=open("%s.m3u"%filename,"w")
    for item in mp3:
        file.write("%s\\%s.mp3\n"%(string,item))
    file.close()
    print "Playlist created"        
    
print
print "Thank you for using PlayList Creator!"
print "Press Enter to Exit."
raw_input()
