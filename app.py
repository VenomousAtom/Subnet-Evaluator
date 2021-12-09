from flask import Flask, request, render_template, url_for
import initiator as initiate
import evaluator as evaluate

app = Flask(__name__)

class pc_details:
    y = 0
    x = 0
    li = []
    switch = []
    k = [0]
    t = 0
    sw_li = []
    pc_li = []
    sw_errors = []
    pc_errors = []
    result=0

ses = pc_details()

@app.route("/", methods=["GET","POST"])
def index():
    ses.y = 0
    ses.x = 0
    ses.li = []
    ses.switch = []
    ses.k = [0]
    ses.t = 0
    ses.sw_li = []
    ses.pc_li = []
    ses.sw_errors = []
    ses.pc_errors = []
    ses.result = 0
    return render_template("index.html",x=ses.x,y=ses.y)

@app.route("/hosts", methods=["GET","POST"])
def hosts():
    if request.method == 'POST':
        ses.x = request.form['switch']
        ses.y = 1
        print(ses.x)
        return render_template("index.html", x=int(ses.x), y=int(ses.y))

@app.route("/home", methods=["GET","POST"])
def home():
    ses.switch = []
    ses.k = [0]
    ses.t=0
    print(ses.x)
    for i in range(int(ses.x)):
        ele = request.form['hosts'+str(i)]
        ses.switch.append(int(ele))
    print(ses.switch)
    for i in ses.switch:
        ses.t += int(i)
        ses.k.append(ses.t)
    value = initiate.initiate(ses.switch)
    ses.sw_li = value["switch"]
    ses.pc_li = value["pc"]
    return render_template("visual copy.html", switch=ses.switch, n=int(len(ses.switch)), temp=int(ses.t), l=ses.k, sw_li=ses.sw_li, pc_li=ses.pc_li)

@app.route("/pc/<int:swt>/<int:pc>", methods=['GET','POST'])
def pcdetails(swt,pc):
    if request.method == 'POST':
        hostip = request.form['hostip']
        sm = request.form['sm']
        dg = request.form['dg']
        # print(swt,pc)
        # print(hostip)
        # print(sm)
        # print(dg)
        ses.pc_li[swt][pc][0] = hostip
        ses.pc_li[swt][pc][1] = sm
        ses.pc_li[swt][pc][2] = dg
        print(swt,pc,ses.pc_li[swt][pc])
        return render_template("visual copy.html", switch=ses.switch, n=len(ses.switch), temp=int(ses.t), l=ses.k, sw_li=ses.sw_li, pc_li=ses.pc_li)

@app.route("/switch/<int:swt>",methods=["GET","POST"])
def switchdetails(swt):
    if request.method=="POST":
        cidr = request.form['cidr']
        dg = request.form['dg']
        # print(swt)
        # print(cidr)
        # print(dg)
        ses.sw_li[swt][0] = dg
        ses.sw_li[swt][1] = int(cidr)
        print(swt, ses.sw_li[swt])
        return render_template("visual copy.html", switch=ses.switch, n=len(ses.switch), temp=int(ses.t), l=ses.k, sw_li=ses.sw_li, pc_li=ses.pc_li)
    
@app.route("/result",methods=["GET","POST"])
def ev():
    if request.method == "POST":
        ses.sw_errors = []
        ses.pc_errors = []
        ses.result=0
        for i in range(len(ses.switch)):
            #evaluate_switch(swt, sw_def, sw_cidr)
            sw_error = evaluate.evaluate_switch(i,ses.sw_li[i][0], ses.sw_li[i][1])
            ses.sw_errors.append(sw_error["switch"])
            if ses.sw_errors[i][1][0]!="OK":
                ses.result=1
            for j in range(ses.switch[i]):
                #evaluate_pc(swt,pc, ip, subnet, def_gate, sw_def, sw_cidr)
                pc_error = evaluate.evaluate_pc(i, j, ses.pc_li[i][j][0], ses.pc_li[i][j][1], ses.pc_li[i][j][2], ses.sw_li[i][0], ses.sw_li[i][1])
                ses.pc_errors.append(pc_error["pc"])
        for i in range(len(ses.pc_errors)):
            if ses.pc_errors[i][2][0]!="OK":
                ses.result=1
        print(ses.sw_errors,ses.pc_errors)
    # return {
    #     "switch": ses.sw_errors,
    #     "pc": ses.pc_errors
    # }
    return render_template("result.html", switch=ses.switch, n=len(ses.switch), temp=int(ses.t), l=ses.k, sw_li=ses.sw_li, pc_li=ses.pc_li, sw_errors=ses.sw_errors, pc_errors=ses.pc_errors, r=ses.result)

if __name__ == "__main__":
    app.run(port=3000,debug=True)

