import requests as req
import json

class Github :
    def __init__(self):
            self.api_url = 'https://api.github.com'
            self.token = 'dc2ef12ff49919e8f869c66a291ef6cf60b06155'
    
    def getUser(self,username) :
        response = req.get(self.api_url+'/users/'+username)      
        return response.json()  
    
    def getRepos(self,username) :
        response = req.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    
    def createRepo(self,name) :
        response = req.post(self.api_url+'/user/repos?access_token='+self.token,json={
            "name" : name,
            "description" :"First Api Repo",
            "homepage" : "https://ogzhn1k.com",
            "private" : False,
            "has_issues" : True,
            "has_projects" : True,
            "has_wiki" : True
        })
        return response.json()
    
    def deleteRepo(self,name) :
        response = req.delete(self.api_url+'/user/repos?access_token='+self.token,json={
            "accept" : "application/vnd.github.v3+json",
            "owner" : 'octocat',
            "repo" : name
        })
        return response.json()

github = Github()

while True :
    option = input('1- Find User\n2- Get Repos\n3- Create Repo\n4- Delete Repo\n5- Exit\nOption : ')
    
    if option == '5' :
        break
          
    else :
        if option == '1' :
            username = input("Please enter the username : ")
            result = github.getUser(username)
            print(f"Name : {result['login']} Public Repos : {result['public_repos']} Followers : {result['followers']}")
            
            
        elif option == '2' :
             username = input("Please enter the username : ")
             result = github.getRepos(username)
             for repo in result :
                 print(repo['name'])
                 
             
        elif option == '3' :
            name = input("Please enter the repo name : ")
            result = github.createRepo(name)
            print(result)
            
        elif option == '4' :
            name = input("Please enter the repo name : ")
            result = github.deleteRepo(name)
            print(result)
                
        else :
            print("Wrong Option!!!")
            



