import os

os.system("cls")
print("""

     )                                 (                                                 
  ( /(          *   )        )         )\ )                   (            (             
  )\())     ( ` )  /(  (  ( /(    (   (()/(      (  (         )\        )  )\ )  (  (    
 ((_)\ (   ))\ ( )(_))))\ )\())  ))\   /(_))  (  )\))(   (   ((_)(   ( /( (()/( ))\ )(   
__ ((_))\ /((_|_(_())/((_|(_)\  /((_) (_))_   )\((_)()\  )\ ) _  )\  )(_)) ((_))((_|()\  
\ \ / ((_|_))(|_   _(_))(| |(_)(_))    |   \ ((_)(()((_)_(_/(| |((_)((_)_  _| (_))  ((_) 
 \ V / _ \ || | | | | || | '_ \/ -_)   | |) / _ \ V  V / ' \)) / _ \/ _` / _` / -_)| '_| 
  |_|\___/\_,_| |_|  \_,_|_.__/\___|   |___/\___/\_/\_/|_||_||_\___/\__,_\__,_\___||_|   
                                                                                       
""")
choice = input("""Select your download option: 
    1. Audio only
    2. Video  
    3. Playlist 
    4. From File

Your selection: """)




if choice == str(1) or choice == "a" or choice == "audio":
    link = input("Paste in the audio URL: ")
    os.system(f"youtube-dl.exe -f best --embed-thumbnail --add-metadata -x {link}")
    
elif choice == str(2) or choice == "v" or choice == "video":
    link = input("Paste in the video URL: ")
    os.system(f"youtube-dl.exe -f best --embed-thumbnail --add-metadata {link}")

elif choice == str(3) or choice == "p" or choice == "playlist":
    link = input("Paste in the playlist URL: ")
    AorV = input("""How would you like the playlist to be downloaded as: 
        1. Audio 
        2. Video
Your selection: """)
    if AorV == str(1) or AorV == "a" or AorV == "audio":
        os.system(f"youtube-dl.exe -f best --embed-thumbnail --add-metadata -a -x -i --yes-playlist {link}")
    elif AorV == str(2) or AorV == "v" or AorV == "video":
        os.system(f"youtube-dl.exe -f best --embed-thumbnail --add-metadata -a -i --yes-playlist {link}")
    else:
        print("Not a valid selection")

elif choice == str(4) or choice == "f" or choice == "file":
    link = input("File to crawl through: ")
    AorV = input("""How would you like the videos to be downloaded as: 
        1. Audio 
        2. Video
Your selection: """)
    if AorV == str(1) or AorV == "a" or AorV == "audio":
        os.system(f"youtube-dl.exe -f best --embed-thumbnail --add-metadata -i -x -a {link}")
    elif AorV == str(2) or AorV == "v" or AorV == "video":
        os.system(f"youtube-dl.exe -f best --embed-thumbnail --add-metadata -i -a {link}")
    else:
        print("Not a valid selection")

else:
    print("Invalid option")
    