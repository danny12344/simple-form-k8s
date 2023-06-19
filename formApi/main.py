from fastapi import FastAPI

app = FastAPI()

@app.post("/test")
def test_endpoint(data: str):
    # Process the received data
    processed_data = data.upper()

    # Return a response
    return {"message": f"Received data: {data}", "processed_data": processed_data}
