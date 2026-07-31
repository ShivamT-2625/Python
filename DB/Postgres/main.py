from fastapi import FastAPI ,APIRouter


app = FastAPI()
router=APIRouter()
@router.get("/")
def hey():
    return {"message":"Hello from server"}


