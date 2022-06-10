from pydantic import BaseModel

class User(BaseModel):
     name: str
     phone: str
     email: str

class Movie(BaseModel):
     mname: str
     released_date: str
     descr: str

class Show(BaseModel):
     start_time: str
     end_time: str
     m_id: int

class Theatre(BaseModel):
     tname: str
     location: str
    
class Seat(BaseModel):
     seat_no: int


class Booking(BaseModel):
     u_id: int
     t_id: int
     show_id: int
     seat_id: int
     show_date: str

     
