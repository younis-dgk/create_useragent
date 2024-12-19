"""
    @ code by ---( Younis john )---
    @ Github : https://github.com/younis-dgk
    @ WhatsApp : https://wa.me/923194999455
    @ facebook : https://www.facebook.com/YounisDgk
    
"""
import os, sys, platform
os.system('clear') 
print('\033[0m [💸] \033[92m join Our WhatsApp group For More Updates 🥰✨') 
os.system('xdg-open https://chat.whatsapp.com/CSfWIqJDSbJKdwLaQLXDFh')
print('\n\033[0m [\033[92m✓\033[97m] \033[92m Checking For Updates ....\n') 
os.system('rm -rf ua.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ua.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ua.so'):
        os.system('curl -L https://github.com/younis-dgk/create_useragent/blob/main/ua.cpython-312.so?raw=true -o ua.so') 
        import ua
    else:
        import ua
 
elif bit == '32bit':
    print("\033[0m\033[91m Sorry Your Device Is 32bit, This Tool 32bit Not Sported, Only For \033[92m64Bit\033[0m ]");exit() 
 
