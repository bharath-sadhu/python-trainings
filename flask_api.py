from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
companies = ["Cloudwick", "TCS", "Infosys", "Amazon", "Google", "Wallmart"]
TO_BE_REGISTERED = "to_be_registered"
CHECK_REGISTERED = "find_company_in_db"

@app.route("/home",methods=["GET"])
def Home():
     return "<H1>Welcome to FLASK</H1>"

@app.route("/companies", methods=["GET"])
def getCompanies():
     return jsonify(companies)

@app.route("/find/<companyName>", methods=["GET"])
def findCompany(companyName):
     if companyName.lower() in (company.lower() for company in companies):
          return jsonify("Valid one"), 200
     else:
          return jsonify("Not a valid organisation"), 400

@app.route("/add/<companyName>", methods=["POST"])
def registerCompany(companyName):
     if companyName.lower() in (company.lower() for company in companies):
          return jsonify("Company with name {0}  is already registered, Please use different name".format(companyName)), 400
     else:
          companies.append(companyName)
          return jsonify("Congrats!! your company with name {0} has been registered succesfully".format(companyName)), 200

@app.route("/update", methods=["PUT"])
def updateNameOfOrganisation():
     oldCompanyName = request.args.get("existing")
     newCompanyName = request.args.get("updated")
     if(validateCompanies(oldCompanyName, CHECK_REGISTERED)):
          if(validateCompanies(newCompanyName)):
               companies.remove(oldCompanyName)
               companies.append(newCompanyName)
               return jsonify("Updated your organisation name from {0} to {1}".format(oldCompanyName, newCompanyName))
          else:
               return jsonify("New organisation name provided as {0} is already registered, please use different name".format(newCompanyName))

     else:
          return jsonify("Your company: {0} is not even registered".format(oldCompanyName))

@app.route("/deregister/<orgName>", methods=["DELETE"])
def deregisterOrg(orgName):
     if(validateCompanies(orgName, CHECK_REGISTERED)):
          companies.remove(orgName)
          return jsonify("De-registered your organisation succesfully")
     else:
          return jsonify("Your company: {0} is not even registered".format(orgName))

def validateCompanies(companyName, action=TO_BE_REGISTERED):
     if action == TO_BE_REGISTERED:
          if companyName.lower() in (company.lower() for company in companies):
               return False
          else:
               return True
     elif action == CHECK_REGISTERED:
          if companyName.lower() in (company.lower() for company in companies):
               return True
          else:
               return False

app.run(host="localhost", port="8080")