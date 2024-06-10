import turtle
import math

import psycopg2
from turtle import *

NITROGEN_LIST = []  # 30 60 120
WATER_LIST = []  # 30 60 120
OIL_LIST = []  # oil - 60 120 240       oil_well - 30 60 120
LIMESTONE_LIST = []  # 30 60 120
URAN_LIST = []  # 30 60 120
BAUXITE_LIST = []  # 30 60 120
QUARTZ_LIST = []  # 30 60 120
SULFUR_LIST = []  # 30 60 120
COAL_LIST = []  # 30 60 120
KATHERIUM_LIST = []  # 30 60 120
COOPER_LIST = []  # 30 60 120
IRON_LIST = []  # 30 60 120
COUNT = 0
turtle.speed('slow')


def polygonAreaPts(pts):
    area = 0
    last = len(pts) - 1
    for i in range(len(pts)):
        area += pts[last][0] * pts[i][1] - pts[last][1] * pts[i][0]
        last = i
    return 0.5*abs(area)


class Resource:
    def __init__(self, rid, x_cord, y_cord, rtype, purity):
        print('Создан объект Resource')
        self.rid = int(rid)
        self.x_cord = int(x_cord),
        self.y_cord = int(y_cord),
        self.rtype = rtype,
        self.purity = purity

    def gettype(self):
        return self.rtype


class Well:
    def __init__(self, rid, x_cord, y_cord, rtype, poor_kol, normal_kol, rich_kol):
        print('Создан объект Well')
        self.rid = rid
        self.x_cord = x_cord,
        self.y_cord = y_cord,
        self.rtype = rtype,
        self.poor_kol = poor_kol,
        self.normal_kol = normal_kol,
        self.rich_kol = rich_kol


try:
    conn = psycopg2.connect(dbname='Satisfactory', user='postgres', password='postgres', host='localhost', port=5432)
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM resources
        FULL OUTER JOIN wells ON resources.id = wells.resource_id
    """)

    for row in cur.fetchall():
        if row[4] == 'complex':
            # wells
            if row[3] == 'oil_well':
                # oil_well
                OIL_LIST.append(
                    Well(int(row[0]), int(row[1]), int(row[2]), str(row[3]), int(row[7]), int(row[8]), int(row[9])))
                COUNT += 1
            elif row[3] == 'nitrogen':
                # nitrogen
                NITROGEN_LIST.append(
                    Well(int(row[0]), int(row[1]), int(row[2]), str(row[3]), int(row[7]), int(row[8]), int(row[9])))
                COUNT += 1
            else:
                # water
                WATER_LIST.append(
                    Well(int(row[0]), int(row[1]), int(row[2]), str(row[3]), int(row[7]), int(row[8]), int(row[9])))
                COUNT += 1
        else:
            # resources
            if row[3] == 'limestone':
                # limestone
                LIMESTONE_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            elif row[3] == 'uran':
                # uran
                URAN_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            elif row[3] == 'bauxite':
                # bauxite
                BAUXITE_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            elif row[3] == 'quartz':
                # quartz
                QUARTZ_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            elif row[3] == 'sulfur':
                # sulfur
                SULFUR_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            elif row[3] == 'coal':
                # coal
                COAL_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            elif row[3] == 'katherium':
                # katherium
                KATHERIUM_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            elif row[3] == 'cooper':
                # cooper
                COOPER_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            elif row[3] == 'iron':
                # iron
                IRON_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1
            else:
                # oil
                OIL_LIST.append(Resource(int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4])))
                COUNT += 1

    if COUNT == 417:
        print('Чтение успешно!')
    else:
        print(f'Чтение не успешно. Прочитанно {COUNT} из 417 элементов!')

    up()
    minP = 5000 * 4
    x1, x2, x3, x4, x5, y1, y2, y3, y4 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    mins, minc, minq = pow(5000, 2), pow(5000, 2), pow(5000, 2)
    for bauxite in BAUXITE_LIST:
        x1, x2, x3, x4, x5, y1, y2, y3, y4 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        mins, minc, minq = pow(5000, 2), pow(5000, 2), pow(5000, 2)
        xb = int(int(''.join(map(str, bauxite.x_cord)))) / 10
        yb = 0 - int(int(''.join(map(str, bauxite.y_cord)))) / 10
        x1 = xb
        y1 = yb
        minq = pow(5000, 2)





        # if math.hypot(x2 - x1, y2 - y1) < math.hypot(x3 - x1, y3 - y1):
        #     if math.hypot(x2 - x1, y2 - y1) < math.hypot(x4 - x1, y4 - y1):
        #         a = math.hypot(x2 - x1, y2 - y1)
        #         if math.hypot(x3 - x2, y3 - y2) < math.hypot(x4 - x2, y4 - y2):
        #             b = math.hypot(x3 - x2, y3 - y2)
        #             c = math.hypot(x4 - x3, y4 - y3)
        #             d = math.hypot(x1 - x4, y1 - y4)
        #         else:
        #             b = math.hypot(x4 - x3, y4 - y3)
        #             c = math.hypot(x3 - x2, y3 - y2)
        #             d = math.hypot(x1 - x4, y1 - y4)
        #
        #     else:
        #         a = math.hypot(x4 - x1, y4 - y1)
        #         if math.hypot(x3 - x2, y3 - y2) < math.hypot(x4 - x2, y4 - y2):
        #             b = math.hypot(x3 - x2, y3 - y2)
        #             c = math.hypot(x4 - x3, y4 - y3)
        #             d = math.hypot(x1 - x4, y1 - y4)
        #         else:
        #             b = math.hypot(x4 - x3, y4 - y3)
        #             c = math.hypot(x3 - x2, y3 - y2)
        #             d = math.hypot(x1 - x4, y1 - y4)
        # else:
        #     if math.hypot(x3 - x1, y3 - y1) < math.hypot(x4 - x1, y4 - y1):
        #         pass
        #         a = math.hypot(x3 - x1, y3 - y1)
        #     else:
        #         pass
        #         a = math.hypot(x4 - x1, y4 - y1)





        a = math.hypot(x2 - x1, y2 - y1)
        b = math.hypot(x3 - x2, y3 - y2)
        c = math.hypot(x4 - x3, y4 - y3)
        d = math.hypot(x1 - x4, y1 - y4)
        P = a + b + c + d
        if P < minP:
            minP = P
            x1 = xb
            y1 = yb



    up()
    goto(x1, y1)
    down()
    dot(5, "red")
    goto(x2, y2)
    dot(5, "green")
    goto(x3, y3)
    dot(5, "black")
    goto(x4, y4)
    dot(5, "blue")
    goto(x1, y1)

    exitonclick()
    conn.commit()

    cur.close()
    conn.close()
except:
    print('Can\'t establish connection to database')