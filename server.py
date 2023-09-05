voted_per_students= int(input("Her öğrencinin kaç adaya oy vereceğini yazınız:"))
ipv4addr=input("Enter IPv4 Address of the device:")
from flask import Flask, render_template, request
import json

App = Flask(__name__,static_url_path='/static')

candidates=json.load(open("candidates.json","r+")) 
json_file=open("candidates.json","a+")

@App.route("/",methods=["GET", "POST"])
def startpage():
    return render_template("startpage.html")
@App.route("/vote",methods=["GET","POST"])
def vote_update():
    if request.method=="GET":
        return render_template("vote.html",no_of_votes=voted_per_students)
    elif request.method=="POST":
        candidates=json.load(open("candidates.json","r+")) 
        json_file=open("candidates.json","a+")
        for i in range(1,voted_per_students+1):
            votedcandidate=request.form["CandidateName"+str(i)]
            candidates[votedcandidate]+=1
        json_data=json.dumps(candidates)
        json_file.seek(0)
        json_file.truncate()
        json_file.write(str(json_data))
        print(json_file)
        return render_template("success.html")

@App.route("/results")
def results():
    with open("candidates.json") as resultsf:
        resultsjson=json.load(resultsf)   
        sortedresults=sorted(resultsjson.items(), key=lambda x:x[1],reverse=True)
        resultsdict= dict(sortedresults)
        no_of_candidates=len(sorted(candidates))
        sortedNames=list(resultsdict.keys())  
        return render_template("results.html",results=resultsdict,ul=no_of_candidates,candidates=sortedNames)

        
if __name__ =="__main__":
    App.run(host=ipv4addr, port="81",threaded=True)
    