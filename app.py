from flask import Flask, jsonify
from flask import render_template
from 数据获取 import *

app = Flask(__name__)

@app.route('/')
def moban():
    return render_template("界面.html")

@app.route('/get_time_data', methods=['GET', 'POST'])
def get_time_data():
    return get_time()

@app.route('/get_history',methods=['GET', 'POST'])
def get_c1():
    sql="SELECT dt,comfirmed,crued,died FROM 疫情数据.history order by dt desc limit 1; "
    res = get_data(sql)
    response = {'comfirmed':int(res[1]), 'crued':int(res[2]), 'died':int(res[3])}
    return jsonify(response)

@app.route('/get_china_map_data', methods=['GET','POST'])
def get_c2_map():
    sql = 'SELECT province,sum(comfirmed) FROM 疫情数据.details Group by province;'
    res = []
    for tup in get_data1(sql):
        res.append({"name": tup[0], "value": tup[1]})
    return jsonify({'data': res})

@app.route('/get_left1_data', methods=['GET', 'POST'])
def get_left1():
    sql = 'SELECT dt,comfirmed,crued,died FROM 疫情数据.history;'
    data = get_data1(sql)
    day, comfirmed, crued, died = [], [], [], []
    for a, b, c, d in data:
        day.append(a.strftime("%y-%m-%d"))
        comfirmed.append(b)
        crued.append(c)
        died.append(d)
    return jsonify({'day': day, 'comfirmed': comfirmed, 'crued': crued, 'died': died})

@app.route('/get_left2_data', methods=['GET', 'POST'])
def get_left2():
    sql = 'SELECT dt,comfirmed_add,suspect_add FROM 疫情数据.history;'
    data = get_data1(sql)
    day, comfirmed_add, suspect_add = [], [], []
    for a, b, c in data:
        day.append(a.strftime("%y-%m-%d"))
        comfirmed_add.append(b)
        suspect_add.append(c)
    return jsonify({'day': day, 'comfirmed_add': comfirmed_add, 'suspect_add': suspect_add})

@app.route('/get_right1_data', methods=['GET','POST'])
def get_right1():
    sql = """SELECT city,comfirmed FROM
            (select city,comfirmed from details
            where update_time=(select update_time from details order by update_time desc limit 1)
            and province not in ("湖北")
            union all
            select province as city,sum(comfirmed) as comfirmed FROM 疫情数据.details
            where update_time=(select update_time from details order by update_time desc limit 1)
            and province in ("北京")group by province) as a
            order by comfirmed DESC LIMIT 5;"""
    data = get_data1(sql)
    city, comfirmed = [], []
    for k, v in data:
        city.append(k)
        comfirmed.append(v)
    return jsonify({'city': city, 'comfirmed':comfirmed})
@app.route('/get_right2_data',methods=['GET','POST'])
def get_right2():
    sql = """SELECT city,comfirmed FROM
            (select city,comfirmed from details
            where update_time=(select update_time from details order by update_time desc limit 1)
            and province in ("湖北")
            union all
            select province as city,sum(comfirmed) as comfirmed FROM 疫情数据.details
            where update_time=(select update_time from details order by update_time desc limit 1)
            and province in ("北京")group by province) as a
            order by comfirmed DESC LIMIT 5;"""
    data = get_data1(sql)
    city, comfirmed = [], []
    for k, v in data:
        city.append(k)
        comfirmed.append(v)
    return jsonify({'city': city, 'comfirmed': comfirmed})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)