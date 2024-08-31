from fastapi import FastAPI, HTTPException
from weather_fetcher import WeatherFetcher

app = FastAPI()

# Initialize the WeatherFetcher class
weather_fetcher = WeatherFetcher()

@app.get("/weather/")
async def get_weather(city_name: str):
    """
    Endpoint to get current weather data for a given city.
    """
    try:
        weather_data = weather_fetcher.get_current_weather(city_name)
        return weather_data
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching weather data.")

# Optional root endpoint to check the API is running
@app.get("/")
async def root():
    return {"message": "Weather API is running. Use /weather/?city_name=CITY_NAME to get weather data."}