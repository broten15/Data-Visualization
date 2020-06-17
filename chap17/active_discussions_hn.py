import requests
import pygal
from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API to store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code:', r.status_code)

# Process information about most active discussions
discussion_ids = r.json()
discussion_dicts = []
for discussion_id in discussion_ids:
    # Gets each discussion
    url = ('https://hacker-news.firebaseio.com/v0/item/' + 
        str(discussion_id) + '.json')
    discussion_r = requests.get(url)
    response_dict = discussion_r.json()

    discussion_dict = {
        'title': response_dict['title'],
        'value': response_dict.get('descendants', 0),
        'xlink': 'http://news.ycombinator.com/item?id=' + str(discussion_id)
        }
    discussion_dicts.append(discussion_dict)

# Sorts discussion dicts by most to least comments
discussion_dicts = sorted(discussion_dicts, key=itemgetter('value'),
                            reverse=True)

# Makes visualization 
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Top 30 most active discussions on Hacker News based on number of comments'
titles = []
for discussion_dict in discussion_dicts[:30]:
    titles.append(discussion_dict['title'])
print(titles)
chart.x_labels = titles

chart.add('', discussion_dicts[:30])
chart.render_to_file('most_active_discussions.svg')



