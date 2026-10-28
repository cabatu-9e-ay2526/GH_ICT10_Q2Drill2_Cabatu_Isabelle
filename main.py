# Q2 Drill 2 
from pyscript import document

def checkresult(e):

    # Predefined club members grouped by grade
    grade7 = {
        'Apple White', 'Raven Queen',
        'Briar Beauty', 'Ashlynn Ella'
    }

    grade8 = {
        'Madeline Hatter', 'Cedar Wood',
        'Cerise Hood', 'Blondie Lockes'
    }

    grade9 = {
        'Hunter Huntsman', 'Dexter Charming',
        'Darling Charming', 'Holly OHair'
    }

    grade10 = {
        'Poppy OHair', 'Kitty Cheshire',
        'Lizzie Hearts', 'Daring Charming'
    }

    firstname = document.getElementById('firstname').value.strip()
    lastname = document.getElementById('lastname').value.strip()

    new_member = (firstname + ' ' + lastname).strip()

    additional_member = {new_member}

    all_members = grade7 | grade8 | grade9 | grade10 | additional_member

    members_list = '<br>'.join(sorted(all_members))

    total_members = len(all_members)

    document.getElementById('output').innerHTML = (
        f'<strong>All Members:</strong><br>{members_list}'
        f'<br><br><strong>Total Members: {total_members}</strong>'
    )