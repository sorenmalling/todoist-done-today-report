import todoist
from datetime import date
import sys

if len(sys.argv) >= 2:
    print 'You must give a token as parameter'
    sys.exit(1)

token = sys.argv[1]

api = todoist.TodoistAPI(token)
today = date.today().isoformat()

completeditems = api.get_all_completed_items(since = today + 'T00:00')

if 'items' in completeditems and len(completeditems['items']) > 0:
    print len(completeditems["items"])
    for d in completeditems["items"]:
        print d["completed_date"] + ' --> ' + d["content"]
else:
    print 'API returned no items'