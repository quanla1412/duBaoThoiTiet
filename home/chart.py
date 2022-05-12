import base64
from io import BytesIO
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
from . import methods


#set cột ngày tháng cho biểu đồ
today = date.today()
x = [str((today - timedelta(7-i)).strftime('%d/%m')) for i in range(8)]

#nhiệt độ theo 7 ngày trước đến hiện tại
def getAllChart(id = 58):

    data = methods.getDailyCity(id)

    allChart = list()

    fig = plt.figure() 
    
    y = [x["temp"] for x in data]

    plt.xlabel('Ngày')
    plt.ylabel('Nhiệt Độ (°C)')
    plt.title('Nhiệt Độ 7 Ngày Trước')
    plt.plot(x,y, color = "red")

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    chart = '<img src=\'data:image/png;base64,{}\' alt="" class="w-100">'.format(encoded)
    allChart.append(chart)


    fig = plt.figure() 

    a = [x["rain"] for x in data]

    plt.xlabel('Ngày')
    plt.ylabel('Lượng Mưa (mm)')
    plt.title('Lượng Mưa 7 Ngày Trước')
    plt.bar(x,a)

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    chart = '<img src=\'data:image/png;base64,{}\' alt="" class="w-100">'.format(encoded)
    allChart.append(chart)


    fig = plt.figure() 

    b = [x["uvi"] for x in data]

    plt.xlabel('Ngày')
    plt.ylabel('Chỉ Số UV')
    plt.title('Chỉ Số UV 7 Ngày Trước')
    plt.bar(x,b, color ="purple")

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    chart = '<img src=\'data:image/png;base64,{}\' alt="" class="w-100">'.format(encoded)
    allChart.append(chart)


    fig = plt.figure() 

    c = [x["clouds"] for x in data]

    plt.title('Lượng Mây 7 Ngày Trước')
    plt.pie(c,labels=x, autopct='%1.1f%%')
    plt.axis('equal')
    

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    chart = '<img src=\'data:image/png;base64,{}\' alt="" class="w-100">'.format(encoded)
    allChart.append(chart)

    return allChart