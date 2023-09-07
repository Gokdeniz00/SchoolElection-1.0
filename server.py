voted_per_students= int(input("Her öğrencinin kaç adaya oy vereceğini yazınız:"))
ipv4addr=input("Enter IPv4 Address of the device:")
from flask import Flask, render_template, request
import sqlite3 as db
from sqlite3 import Error

App = Flask(__name__,static_url_path='/static')

#candidates=json.load(open("candidates.json","r+")) 

#json_file=open("candidates.json","a+")

@App.route("/",methods=["GET", "POST"])
def startpage():
    return render_template("startpage.html")
@App.route("/vote",methods=["GET","POST"])
def vote_update():
    if request.method=="GET":
        return render_template("vote.html",no_of_votes=voted_per_students)
    elif request.method=="POST":
        try:
            candidatesdatabase=db.connect("candidate.db")
        except Error as e:
            print(e)
        cursor=candidatesdatabase.cursor()        
        for i in range(1,voted_per_students+1):
            votedcandidate=request.form["CandidateName"+str(i)]
            cursor.execute(f'''SELECT VOTES 
                           FROM CANDIDATE
                           WHERE NAME='{votedcandidate}';
''')
            votes=cursor.fetchone()
            if votes:
                cursor.execute(f'''
                            UPDATE CANDIDATE
                            SET VOTES={votes[0]+1}
                            WHERE NAME='{votedcandidate}';
                ''')            
                candidatesdatabase.commit()  
            else:
                return render_template(f"<h1> NO CANDIDATE NAMED {votedcandidate}!!!!!")

        return render_template("success.html")

@App.route("/results")
def results():
    try:
        candidatesdatabase=db.connect("candidate.db")
    except Error as e:
        print(e)
    cursor=candidatesdatabase.cursor()
    cursor.execute(f'''
        SELECT * FROM CANDIDATE
        ORDER BY VOTES DESC;
''')
    results=cursor.fetchall()
    succesors=[x for x in results]
    return render_template("results.html",results=succesors)

        
if __name__ =="__main__":
    App.run(host=ipv4addr, port=81,threaded=True)