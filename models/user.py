from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Table,Column,ForeignKey
from sqlalchemy.orm import relationship
from config.db import meta
users = Table(
    'users',meta,
    Column('u_id',Integer,primary_key = True),
    Column('name',String(255)),
    Column('phone',String(255)),
    Column('email',String(255)),
)

movies = Table(
    'movies',meta,
    Column('m_id',Integer,primary_key = True),
    Column('mname',String(255)),
    Column('released_date',String(255)),
    Column('descr',String(255)),
)
shows = Table(
    'shows',meta,
    Column('show_id',Integer,primary_key = True),
    Column('start_time',String(255)),
    Column('end_time',String(255)),
    Column('m_id',Integer,ForeignKey('movies.m_id', ondelete='CASCADE')),
)
theatres = Table(
    'theatres',meta,
    Column('t_id',Integer,primary_key = True),
    Column('tname',String(255)),
    Column('location',String(255)),
)
seats = Table(
    'seats',meta,
    Column('seat_id',Integer,primary_key = True),
    Column('seat_no',Integer),  
)
bookings = Table(
    'bookings',meta,
    Column('b_id',Integer,primary_key = True),
    Column('seat_no',Integer),
    Column('show_date',String(255)),
    Column('show_id',Integer,ForeignKey('shows.show_id', ondelete='CASCADE')),
    Column('u_id',Integer,ForeignKey('users.id', ondelete='CASCADE')),
    Column('seat_id',Integer,ForeignKey('seats.seat_id', ondelete='CASCADE')),
    Column('t_id',Integer,ForeignKey('theatres.t_id', ondelete='CASCADE')),
)

