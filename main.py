import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return RedirectResponse("/static/index.html")


@app.get("/api/basestation/on")
async def basestation_on():
    await send(b'\x01')
    return "on"


@app.get("/api/basestation/off")
async def basestation_on():
    await send(b'\x00')
    return "off"


async def send(status):
    # TODO: implement here
    print('SEND:    ', status)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
