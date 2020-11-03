def runtime():
    greeting = "Welcome to Noah's Project"
    name = "Repl"
    job = "Runtime Link"
    embed = "https://Flask-Website-Project.noahahooja.repl.co"
    info = {"greeting": greeting, "name": name, "job": job, "embed": embed}
    return info

def planning():
    greeting = "Hi!"
    name = "Padlet"
    job = "Project Planning"
    embed = "https://padlet.com/jmortensen7/csptime1_2"
    info = {"greeting": greeting, "name": name, "job": job, "embed": embed}
    return info

def journal():
    greeting = "Journal"
    name = "Google Doc"
    job = "Journal Record"
    embed = "https://docs.google.com/document/d/1vaG4nyI1oJhL8I3tl_YtNfT0xXNU3FGKKNGN1Yadma0/edit"
    info = {"greeting": greeting, "name": name, "job": job, "embed": embed}
    return info


def code():
    greeting = "Code Section"
    name = "Gist"
    job = "Code Sample"
    gist = "https://gist.github.com/jm1021/cfb277c7357e02fcb4123a6c7429a5c1.js"
    info = {"greeting": greeting, "name": name, "job": job, "gist": gist}
    return info

def alldata():
    return [runtime(), planning(), journal(), code()]

#Data "setup" for Projects
#next step would be to extract project data from a database
def setup():
    #Source Data
    name = "Nighthawk Coding"
    github = "https://github.com/nighthawkcoders"
    linkedin = "https://www.linkedin.com/in/john-mortensen-1021/"
    youtube = "https://www.youtube.com/channel/UClIKOsDS5dsfzFA3zveDT3Q?view_as=subscriber"
    twitter = "https://twitter.com/NighthawkCoding"
    source = {"name": name, "github": github, "linkedin": linkedin, "youtube": youtube, "twitter": twitter}
    #Project Data
    project1 =  "Arcade"
    projlinks1 = [
        Link("Project Plan", "https://docs.google.com/document/d/168LMTHNHsrdtSSya1NUOy9lBK3ezxl6BiGeg_utE8IA/edit"),
        Link("Repl", "https://repl.it/@NolanDEsopo/Games#main.py"),
        Link("Resources", "https://padlet.com/jmortensen7/csp2021")
    ]
    project2 =  "Flask Project"
    projlinks2 = [
        Link("Project Plan", "https://docs.google.com/document/d/1xwbOqk9I-5DXH8NvxgTX13KvAgK13SI8XJTYfEbIgUM/edit"),
        Link("Repl", "https://repl.it/@NoahAhooja/Flask-Website-Project#main.py"),
        Link("Resources", "https://padlet.com/jmortensen7/csptime1_2")
    ]
    #Project Objects
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    #HTML Data
    projects = Projects(source, [proj1, proj2])
    return projects

#Link class contains button (label) and hypertext reference (href)
class Link():
    #link data with button and href (url)
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href
    def get_btn(self):
        return self.btn
    def get_href(self):
        return self.href

#Project data class contain project name and links (Link class objects)
class Project():
    #project data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links
    def get_name(self):
        return self.name
    def get_links(self):
        return self.links

#Projects class contains person (owner) and multiple projects (Project class objects)
class Projects():
    #HTML data with source and projects
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects
    #source data getter
    def get_source(self):
        return self.source
    #project data getter
    def get_projects(self):
        return self.projects