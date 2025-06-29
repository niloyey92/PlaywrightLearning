from configparser import ConfigParser

# config=ConfigParser()
# config.read("config.ini")
# print(config.get("locator","userIcon"))
# print(config.get("basic info","url"))

def readConfig(section,key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section,key)

print(readConfig("locator","userIcon"))