import re
from termcolor import colored
from lib.core.common import HTTP_HEADER
print("  =====================          ")  
print("| Wi-fi Deauthenticator |        ") 
print("  =====================          ")  
print("       \                         ")  
print("        \                        ")  
print("         \                       ") 
print("          .--.                   ")   
print("         |o_o |                  ")
print("         |:_/ |                  ")
print("        //   \ \                 ")    
print("       (|     | )                ")
print("      /'\_   _/`\                ") 
print("      \___)=(___/                ")  
print("                                 ")
print("                                 ")
print(colored("       By JOKER  ",'green'))
print("                                 ")


__item__ = "CloudFlare Web Application Firewall (CloudFlare)"


def detect(content, **kwargs):
    headers = kwargs.get("headers", None)
    content = str(content)
    detection_schemas = (
        re.compile(r"CloudFlare Ray ID:|var CloudFlare=", re.I),
        re.compile(r"cloudflare-nginx", re.I),
        re.compile(r"\A__cfduid=", re.I),
        re.compile(r"CF_RAY", re.I)
    )
    for detection in detection_schemas:
        if detection.search(content) is not None:
            return True
        elif detection.search(headers.get(HTTP_HEADER.SERVER, "")) is not None:
            return True
        elif detection.search(headers.get(HTTP_HEADER.COOKIE, "")) is not None:
            return True
        elif detection.search(str(headers)) is not None:
            return True
