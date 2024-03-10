from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=schemas.User)
def read_user(name: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name_by_password(db, name=name, password=password)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/sales/", response_model=schemas.Sales)
def create_sales(sales: schemas.SalesCreate, db: Session = Depends(get_db)):
    db_sales = crud.get_sales_by_year_by_department(db, year=sales.year, department=sales.department)
    if db_sales is None:
        raise HTTPException(status_code=404, detail="Sales not found")
    return crud.create_sales(db=db, sales=sales)


@app.get("/sales/", response_model=list[schemas.Sales])
def read_sales(db: Session = Depends(get_db)):
    sales = crud.get_sales(db)
    return sales


@app.get("/sales/{year}", response_model=list[schemas.Sales])
def read_sales_by_year(year: int, db: Session = Depends(get_db)):
    sales = crud.get_sales_by_year(db, year=year)
    return sales