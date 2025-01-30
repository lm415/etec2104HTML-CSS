import cherrypy
import os.path
import mako.template
#we have modules for each page we're displaying 
import page_signup
import page_posts
import page_test
import random
import datetime

names = ["Alice","Bob","Carol","Dave"]

def random_date():
    x = datetime.timedelta(minutes=random.randrange(8000))
    hoursago = int( x.seconds / 3600 )
    minutesago = round( (x.seconds - hoursago*3600)/ 60)
    views = random.randint(0,100)
    return f"Posted:{x.days} days, {hoursago} hours, and {minutesago} minutes ago, Views: {views}"


PYPATH = os.path.dirname(__file__)

class App:
    @cherrypy.expose
    def index(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/page_index.html")
        n = random.choice(names)
        return t.render(NAME=n)

    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    
    @cherrypy.expose
    def posts(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/page_posts.html")
        date = random_date()
        date2 = random_date()
        date3 = random_date()
        date4 = random_date()
        date5 = random_date()
        date6 = random_date()
        date7 = random_date()
        date8 = random_date()
        date9 = random_date()
        date10 = random_date()
        return t.render(DATE=date, DATE2=date2, DATE3=date3, DATE4=date4, DATE5=date5,  
                        DATE6=date6, DATE7=date7, DATE8=date8, DATE9=date9, DATE10=date10)
    
    @cherrypy.expose
    def test(self):
        return page_test.get()
        
#the location where the main.py file is stored: The src folder
srcdir = os.path.abspath(os.path.dirname(__file__))

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)

