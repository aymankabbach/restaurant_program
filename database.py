from sqlalchemy import create_engine,update,select,Column,Integer,String,Float,Boolean,PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.mutable import MutableList
engine=create_engine('sqlite:///database.sqlite', echo=True)
base=declarative_base()
class Food(base):
    __tablename__="Food"
    id=Column(Integer, primary_key=True)
    name=Column(String(250),nullable=False)
    type=Column(String(250),nullable=False)
    price=Column(Float,nullable=False)

    def __init__(self,name,type,price):
        self.name=name
        self.type=type
        self.price=price
class Drinks(base):
    __tablename__="Drinks"
    id=Column(Integer, primary_key=True)
    name=Column(String(250),nullable=False)
    size=Column(String(250))
    price=Column(Float,nullable=False)

    def __init__(self,name,size,price):
        super().__init__()
        self.name=name
        self.size=size
        self.price=price
class Table(base):
    __tablename__="Tables"
    id=Column(Integer, primary_key=True)
    number=Column(Integer,nullable=False)
    seats=Column(Integer,nullable=False)
    order = Column(MutableList.as_mutable(PickleType),
                                        default=[])
    empty=Column(Boolean,nullable=False)

class Order(base):
        __tablename__="Orders"
        id=Column(Integer, primary_key=True)
        number=Column(Integer,unique=True,nullable=False)
        table_number=Column(Integer,nullable=False)
        order = Column(MutableList.as_mutable(PickleType),
                                        default=[])
        total=Column(Float,nullable=False)
        paid=Column(Boolean,nullable=False)
        canceled=Column(Boolean,nullable=False)
#####
try:
    base.metadata.create_all(engine)
except:
    pass
db=sessionmaker(bind=engine)
session=db()
def get_number_orders():
    targed_table=select(Order)
    number=0
    with engine.connect() as conn:
        for row in conn.execute(targed_table):
            number=row.id
    return number
def create_new_row(table_number,order,total):
    number=get_number_orders()
    new_order=Order(number=number+1,table_number=table_number,order=order
    ,total=total,paid=False,canceled=False)
    session.add(new_order)
    session.commit()
def create_new_tables():
    for number in range(1,6):
        new_table=Table(number=number,seats=4,order=[],empty=True)
        session.add(new_table)
    session.commit()
def update_table(table_number,order,empty):
    stmt = (
    update(Table).\
    where(Table.number == table_number).\
    values(order=order,empty=empty)
    )
    session.execute(stmt)
    session.connection()      
    session.commit()
    session.close()
def update_order(table_number,new_table_number):
    stmt = (
    update(Order).\
    where(Order.table_number == table_number).\
    values(table_number=new_table_number))            
    session.execute(stmt)  
    session.connection()     
    session.commit()
    session.close()