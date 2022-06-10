from fastapi import APIRouter
from config.db import conn
import sqlalchemy
from sqlalchemy import func,select
from models.index import users,movies,bookings,theatres,seats,shows
from schemas.index import User,Movie,Booking,Seat,Theatre,Show
user = APIRouter()
@user.get("/users/")
async def read_data():
    return conn.execute(users.select()).fetchall()
    
@user.get("/users/{id}")
async def read_data1(id:int):
    return conn.execute(users.select().where(users.c.u_id == id)).fetchall()

@user.post("/users/")
async def write_data(user:User):
    conn.execute(users.insert().values(
        name=user.name,
        phone=user.phone,
        email=user.email
    ))
    return conn.execute(users.select()).fetchall()

@user.put("/users/{id}")
async def update_data(id:int,user:User):
    conn.execute(users.update().values(
        name=user.name,
        phone=user.phone,
        email=user.email
    ).where(users.c.u_id == id))
    return conn.execute(users.select()).fetchall()

@user.delete("/users/{id}")
async def delete_data(id:int):
    conn.execute(users.delete().where(users.c.u_id == id))
    return conn.execute(users.select()).fetchall()

@user.get("/movies/")
async def read_data():
    return conn.execute(movies.select()).fetchall()
    
@user.get("/movies/{m_id}")
async def read_data1(m_id:int):
    return conn.execute(movies.select().where(movies.c.m_id == m_id)).fetchall()

@user.post("/movies/")
async def write_data(movie:Movie):
    conn.execute(movies.insert().values(
        mname=movie.mname,
        descr=movie.descr,
        released_date=movie.released_date
    ))
    return conn.execute(movies.select()).fetchall()

@user.put("/movies/{m_id}")
async def update_data(m_id:int,movie:Movie):
    conn.execute(movies.update().values(
        mname=movie.mname,
        descr=movie.descr,
        released_date=movie.released_date
    ).where(movies.c.m_id == m_id))
    return conn.execute(movies.select()).fetchall()

@user.delete("/movies/{m_id}")
async def delete_data(m_id:int):
    conn.execute(movies.delete().where(movies.c.m_id == m_id))
    return conn.execute(movies.select()).fetchall()



@user.get("/shows/")
async def read_data():
    return conn.execute(shows.select()).fetchall()
    
@user.get("/shows/{show_id}")
async def read_data1(show_id:int):
    return conn.execute(shows.select().where(shows.c.show_id == show_id)).fetchall()

@user.post("/shows/")
async def write_data(show:Show):
    conn.execute(shows.insert().values(
      start_time=show.start_time,
      end_time=show.end_time,
      m_id=show.m_id
    ))
    return conn.execute(shows.select()).fetchall()

@user.put("/shows/{show_id}")
async def update_data(show_id:int,show:Show):
    conn.execute(shows.update().values(
      start_time=show.start_time,
      end_time=show.end_time,
      m_id=show.m_id
    ).where(shows.c.show_id == show_id))
    return conn.execute(shows.select()).fetchall()

@user.delete("/shows/{show_id}")
async def delete_data(show_id:int):
    conn.execute(shows.delete().where(shows.c.show_id == show_id))
    return conn.execute(shows.select()).fetchall()


@user.get("/theatres/")
async def read_data():
    return conn.execute(theatres.select()).fetchall()
    
@user.get("/theatres/{t_id}")
async def read_data1(t_id:int):
    return conn.execute(theatres.select().where(theatres.c.t_id == t_id)).fetchall()

@user.post("/theatres/")
async def write_data(theatre:Theatre):
    conn.execute(theatres.insert().values(
      tname=theatre.tname,
      location=theatre.location,
    ))
    return conn.execute(theatres.select()).fetchall()

@user.put("/theatres/{t_id}")
async def update_data(t_id:int,theatre:Theatre):
    conn.execute(theatres.update().values(
      tname=theatre.tname,
      location=theatre.location,
    ).where(theatres.c.t_id == t_id))
    return conn.execute(theatres.select()).fetchall()

@user.delete("/theatres/{t_id}")
async def delete_data(t_id:int):
    conn.execute(theatres.delete().where(theatres.c.t_id == t_id))
    return conn.execute(theatres.select()).fetchall()




@user.get("/seats/")
async def read_data():
    return conn.execute(seats.select()).fetchall()
    
@user.get("/seats/{seat_id}")
async def read_data1(seat_id:int):
    return conn.execute(seats.select().where(seats.c.seat_id == seat_id)).fetchall()

@user.post("/seats/")
async def write_data(seat:Seat):
    conn.execute(seats.insert().values(
      seat_no=seat.seat_no,
    ))
    return conn.execute(seats.select()).fetchall()

@user.put("/seats/{seat_id}")
async def update_data(seat_id:int,seat:Seat):
    conn.execute(seats.update().values(
      seat_no=seat.seat_no,
    ).where(seats.c.seat_id == seat_id))
    return conn.execute(seats.select()).fetchall()

@user.delete("/seats/{seat_id}")
async def delete_data(seat_id:int):
    conn.execute(seats.delete().where(seats.c.seat_id == seat_id))
    return conn.execute(seats.select()).fetchall()



@user.get("/bookings/")
async def read_data():
    return conn.execute(bookings.select()).fetchall()
    
@user.get("/bookings/{b_id}")
async def read_data1(b_id:int):
    return conn.execute(bookings.select().where(bookings.c.b_id == b_id)).fetchall()

@user.post("/bookings/")
async def write_data(booking:Booking):
    query = select(func.count(bookings.c.b_id)).filter(bookings.c.seat_id ==booking.seat_id).filter(bookings.c.t_id ==booking.t_id).filter(bookings.c.show_date==booking.show_date).filter(bookings.c.show_id==booking.show_id)
    s = conn.execute(query).scalar()
    print(s)
    if s==0:
        conn.execute(bookings.insert().values(
                t_id=booking.t_id,
                seat_id=booking.seat_id,
                seat_no=booking.seat_id,
                show_id=booking.show_id,
                u_id=booking.u_id,
                show_date=booking.show_date,
            ))
        return conn.execute(bookings.select()).fetchall()
    else:
        return ("Oops seat booked!!!try with other seat number")

@user.put("/bookings/{b_id}")
async def update_data(b_id:int,booking:Booking):
    q=conn.execute(bookings.select().where(bookings.c.b_id == b_id)).fetchone()
    print(q)
    query = select(func.count(bookings.c.b_id)).filter(bookings.c.seat_id ==booking.seat_id).filter(bookings.c.t_id ==booking.t_id).filter(bookings.c.show_date==booking.show_date).filter(bookings.c.show_id==booking.show_id)
    s = conn.execute(query).scalar()
    print(s)
    if (q[1]==booking.seat_id and q[2]==booking.show_date and q[3]==booking.show_id and q[6]==booking.t_id):
        conn.execute(bookings.update().values(
        t_id=booking.t_id,
        seat_id=booking.seat_id,
        show_id=booking.show_id,
        seat_no=booking.seat_id,
        u_id=booking.u_id,
        show_date=booking.show_date,
        ).where(bookings.c.b_id == b_id))
        return conn.execute(bookings.select()).fetchall()
    elif s==0:
        conn.execute(bookings.update().values(
        t_id=booking.t_id,
        seat_id=booking.seat_id,
        show_id=booking.show_id,
        seat_no=booking.seat_id,
        u_id=booking.u_id,
        show_date=booking.show_date,
        ).where(bookings.c.b_id == b_id))
        return conn.execute(bookings.select()).fetchall()
    else:
        return ("Oops seat booked!!!try with other seat number")

@user.delete("/bookings/{b_id}")
async def delete_data(b_id:int):
    conn.execute(bookings.delete().where(bookings.c.b_id == b_id))
    return conn.execute(bookings.select()).fetchall()