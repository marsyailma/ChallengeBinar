from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def index():
    return JSONResponse(
        content = {
            "ok": True,
            "code": 200,
            "data": {"version": "1.0.0"},
            "message": "success"
        }
    )


from routes import analytics
from routes import cleansing
app.include_router(analytics.router, tags=["Analytics"])
app.include_router(cleansing.router, tags=["Cleansing"])
