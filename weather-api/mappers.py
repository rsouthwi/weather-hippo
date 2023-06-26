from enum import Enum

class Weather(Enum):
    CLEAR = "clear"
    CLOUDY = "cloudy"
    FOG = "foggy"
    THUNDER = "thundering"
    SLEET = "sleeting"
    RAIN = "raining"
    SNOW = "snowing"

# these are available at https://www.weatherapi.com/docs/conditions.json
weather_api_mapping = {
    1000: Weather.CLEAR,
    1003: Weather.CLEAR,
    1006: Weather.CLOUDY,
    1009: Weather.CLOUDY,
    1030: Weather.FOG,
    1135: Weather.FOG,
    1147: Weather.FOG,
    1087: Weather.THUNDER,
    1273: Weather.THUNDER,
    1276: Weather.THUNDER,
    1279: Weather.THUNDER,
    1282: Weather.THUNDER,
    1069: Weather.SLEET,
    1072: Weather.SLEET,
    1168: Weather.SLEET,
    1171: Weather.SLEET,
    1198: Weather.SLEET,
    1201: Weather.SLEET,
    1204: Weather.SLEET,
    1207: Weather.SLEET,
    1249: Weather.SLEET,
    1252: Weather.SLEET,
    1063: Weather.RAIN,
    1150: Weather.RAIN,
    1153: Weather.RAIN,
    1180: Weather.RAIN,
    1183: Weather.RAIN,
    1186: Weather.RAIN,
    1189: Weather.RAIN,
    1192: Weather.RAIN,
    1195: Weather.RAIN,
    1240: Weather.RAIN,
    1243: Weather.RAIN,
    1246: Weather.RAIN,
    1066: Weather.SNOW,
    1114: Weather.SNOW,
    1117: Weather.SNOW,
    1210: Weather.SNOW,
    1213: Weather.SNOW,
    1216: Weather.SNOW,
    1219: Weather.SNOW,
    1222: Weather.SNOW,
    1225: Weather.SNOW,
    1237: Weather.SNOW,
    1255: Weather.SNOW,
    1258: Weather.SNOW,
    1261: Weather.SNOW,
    1264: Weather.SNOW
}