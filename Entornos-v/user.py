from sqlmodel import  SQLModel,Field

class UserModel(SQLModel, table=True):
    __tablename__= "users"

    id: int = Field(primary_key=True)
    name: str
    last_name: str
    email: str
    phone: str