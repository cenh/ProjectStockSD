from Member.models import * # Is this how its done?

# TODO:
# Add Getters: Members, Projects, Groups, Projects from Group, Projects from Subject,
# Projects from Member, Archived Projects, Articles from Group, Articles from Member,
# Presentations from Member, Activities from Member, Upcoming Activities/Presentations
# Add Setters: Member fields, Group fields, Membership fields, Project fields, Presentation fields,
# Activity fields, Article fields

### GETTERS
def getMembers():
    return list(Member.objects.all().order_by('last_name'))

def getMember(l_name):
    return Member.objects.filter(last_name__startswith=l_name)

### SETTERS
def addMember(l_name, f_name, email, site, loc, work, status, tel, bio):
    m = Member(l_name, f_name, email, site, loc, work, status, tel, bio)
    m.save()
