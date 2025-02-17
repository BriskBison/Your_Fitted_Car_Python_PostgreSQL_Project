import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# I am sharing this project publicly,
# for data protection reasons I have to hide the password and port.
# You can find them in the database in Postgre SQL -> right-click on "server" on the left
# -> select "properties" -> "connection" tab

CONN =  psycopg2.connect(
        dbname="your_fitted_car_data",
        user="postgres",
        password="*****",
        host="localhost")
CUR = CONN.cursor()

database="your_fitted_car_data",
user="postgres",
password="****", #
host="localhost"
port="****"

connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(connection_string)

class Data():

    def table1(self):
        CUR.execute("""
                CREATE TABLE IF NOT EXISTS cars (
                car_id SERIAL PRIMARY KEY,
                car_name VARCHAR(30) NOT NULL,
                country TEXT CONSTRAINT country_check CHECK (country IN ('Italian', 'German', 'Japanese', 'American'))        
                )
        """)
        CONN.commit()

    def enum(self):

        CUR.execute("""
                DO $$
                    BEGIN
                    IF NOT EXISTS (SELECT 1 FROM pg_enum WHERE enumtypid = 'class_enum'::regtype 
                    AND enumlabel = 'archived') THEN
                    ALTER TYPE class_enum ADD VALUE 'archived';
                    END IF;
                END $$;
            """)
        CONN.commit()


    def table2(self):
        CUR.execute("""
                CREATE TABLE IF NOT EXISTS features (
                car_id SERIAL PRIMARY KEY,
                class class_enum NOT NULL,
                features TEXT[]
                )
            """)
        CONN.commit()

    def values1(self):
        CUR.execute("""
                    INSERT INTO cars
                    (car_id, car_name, country) 
                    VALUES 
                    (1, 'Dodge RAM', 'American'),
                    (2, 'Jeep Cherokee', 'American'),
                    (3, 'Toyota Hilux', 'Japanese'),
                    (4, 'Nissan Skyline GTR', 'Japanese'),
                    (5, 'Enzo Ferrari', 'Italian'),
                    (6, 'Lamborghini Aventador', 'Italian'),
                    (7, 'Toyota Supra', 'Japanese'),
                    (8, 'BMW Serie 3', 'German'),
                    (9, 'Nissan 350z', 'Japanese')
                    ON CONFLICT (car_id) DO NOTHING
                """)
        CONN.commit()

    def values2(self):
        CUR.execute("""
                    INSERT INTO features
                    (car_id, class, features) 
                    VALUES 
                    (1, 'off-road', ARRAY['safe', 'comfortable', 'long-lived', 'five-door', 'automatic']),
                    (2, 'off-road', ARRAY['safe', 'cheap', 'five-door']),
                    (3, 'off-road', ARRAY['safe', 'economic', 'long-lived', 'five-door', 'automatic']),
                    (4, 'speed', ARRAY['quite_safe','comfortable', 'three-door', 'long-lived', 'automatic']),
                    (5, 'speed', ARRAY['comfortable', 'three-door']),
                    (6, 'speed', ARRAY['comfortable', 'three-door']),
                    (7, 'drift', ARRAY['quite_safe', 'cheap', 'three-door', 'economic', 'long-lived']),
                    (8, 'drift', ARRAY['quite_safe', 'cheap', 'economic', 'five-door', 'long-lived']),
                    (9, 'drift', ARRAY['quite_safe','economic', 'three-door', 'automatic'])
                    ON CONFLICT (car_id) DO NOTHING
                """)
        CONN.commit()

    def query1(self):
        query = """
                SELECT
                c.car_name,
                f.class,
                f.features,
                COUNT(c.country)
                FROM cars c
                LEFT JOIN features f
                ON c.car_id = f.car_id
                WHERE c.country = 'American'
                GROUP BY c.car_name, f.class, f.features
        """
        df = pd.read_sql(query, CONN)
        print(df)

    def query2(self):
        query = """
                SELECT
                car_id,
                country,
                MAX(car_name) OVER(PARTITION BY country) as avg_car_name
                FROM cars
                ORDER BY avg_car_name
        """
        df = pd.read_sql(query, CONN)
        print(df)

    def query3(self):
        query = """
                SELECT DISTINCT
                class,
                car_name,
                features,
                COUNT(class) OVER(PARTITION BY features) as amount
                FROM features f
                LEFT JOIN cars c
                ON c.car_id = f.car_id
                ORDER BY amount DESC
        """
        df = pd.read_sql(query, CONN)
        print(df)

    def query4(self):
        query = """
                SELECT
                CASE 
                WHEN country IN ('American', 'Japanese')
                AND class IN ('speed', 'off-road')
                THEN 'good'
                ELSE 'wrong'
                END as check,
                c.car_name
                FROM cars c
                LEFT JOIN features f
                ON c.car_id = f.car_id
        """
        df = pd.read_sql(query, CONN)
        print(df)

    def query5(self):
        query = """
                SELECT
                car_name,
                country,
                class,
                ROW_NUMBER() OVER (ORDER BY class DESC)
                FROM cars
                NATURAL LEFT JOIN features
                GROUP BY country, car_name, class
        """
        df = pd.read_sql(query, CONN)
        print(df)