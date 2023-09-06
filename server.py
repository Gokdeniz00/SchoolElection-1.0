voted_per_students= int(input("Her öğrencinin kaç adaya oy vereceğini yazınız:"))
ipv4addr=input("Enter IPv4 Address of the device:")
from flask import Flask, render_template, request
import sqlite3 as db

App = Flask(__name__,static_url_path='/static')

#candidates=json.load(open("candidates.json","r+")) 
try:
    candidatesdatabase=db.connect("candidates.db")
except Error as e:
    print(e)
cursor=candidatesdatabase.cursor()
#json_file=open("candidates.json","a+")

@App.route("/",methods=["GET", "POST"])
def startpage():
    return render_template("startpage.html")
@App.route("/vote",methods=["GET","POST"])
def vote_update():
    if request.method=="GET":
        return render_template("vote.html",no_of_votes=voted_per_students)
    elif request.method=="POST":
        #for row in        
        for i in range(1,voted_per_students+1):
            votedcandidate=request.form["CandidateName"+str(i)]
            cursor.execute(f'''SELECT VOTES 
                           FROM CANDIDATES 
                           WHERE NAME={votedcandidate};
''')
            votes=cursor.fetchone()
            if votes:
                cursor.execute(f'''
                            UPDATE CANDIDATES
                            SET VOTES={votes+1}
                            WHERE NAME={votedcandidate};
''')        
            else:
                return render_template(f"<h1> NO CANDIDATE NAMED {votedcandidate}!!!!!")

        return render_template("success.html")

@App.route("/results")
def results():
    cursor.execute(f'''
        SELECT * FROM CANDIDATES
        ORDER BY VOTES DESC;
''')
    no_of_candidates=input("Kaç kaptan seçileceğini giriniz:")
    results=cursor.fetchall()
    succesors=[x for x in results[:no_of_candidates]]
    return render_template("results.html",results=succesors)

        
if __name__ =="__main__":
    App.run(host=ipv4addr, port="81",threaded=True)
    