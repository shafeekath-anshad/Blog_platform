class Authors:
    def __init__(self,username,country):
        self.username=username
        self.country=country
    def profile(self):
        print(self.username,"from",self.country,"has posted on her timeline\n")


class Blog_posts:
    def __init__(self,post):
        self.post=post
    def add_post(self):
        print(self.post)

class Comments:
    def __init__(self,comments):
        self.comments=comments
    def comment(self):
        print("------------")
        print("comments")
        print("------------")
        print(self.comments)

auth_obj=Authors("Anjali","India")
auth_obj.profile()
post_obj=Blog_posts("Hi, I'm Anjali. We are hiring HR Coordinators.")
post_obj.add_post()
comm_obj=Comments("Interested for this oppertunity.")
comm_obj.comment()