# %%
import pandas as pd
import requests
import numpy as np

pd.options.display.max_columns = None
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json = r.json()
json.keys()

# %%
elements_df = pd.DataFrame(json['elements'])
elements_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])
print(elements_df.head())

# %%
#slim_elements_df.sort_values('value',ascending=False).head(5100)
# %%JK
slim_elements_df = elements_df[['second_name', 'team', 'element_type', 'selected_by_percent', 'now_cost', 'minutes', 'transfers_in', 'value_season', 'total_points']]
# %%
print(slim_elements_df.head())
# %%
slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)
# %%
slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
# %%
slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
# %%
slim_elements_df.sort_values('value',ascending=False).head(10)
# %%
pivot = slim_elements_df.pivot_table(index='position',values='value',aggfunc=np.mean).reset_index()
pivot.sort_values('value', ascending=False)
# %%
slim_elements_df = slim_elements_df.loc[slim_elements_df.value > 0]
# %%
pivot = slim_elements_df.pivot_table(index='position',values='value',aggfunc=np.mean).reset_index()
# %%
pivot.sort_values('value',ascending=False)
# %%
team_pivot = slim_elements_df.pivot_table(index='team',values='value',aggfunc=np.mean).reset_index()
team_pivot.sort_values('value',ascending=False)
# %%
fwd_df = slim_elements_df.loc[slim_elements_df.position == 'Forward']
mid_df = slim_elements_df.loc[slim_elements_df.position == 'Midfielder']
def_df = slim_elements_df.loc[slim_elements_df.position == 'Defender']
gk_df = slim_elements_df.loc[slim_elements_df.position == 'Goalkeeper']
# %%
# %%
gk_df.sort_values('value', ascending=False).head(10)
# %%
def_df.sort_values('value', ascending=False).head(10)
# %%
mid_df.sort_values('value', ascending=False).head(10)
# %%KJ
fwd_df = fwd_df.sort_values('value', ascending=False).head(10)
# %%
print(fwd_df)



# %%
fowards = fwd_df['second_name'].tolist()
# %%
print(fowards)
# %%
# %%
fw = fwd_df.set_index('second_name').T.to_dict('list')
print(fw)
# %%   
# %%
fd = dict(list(fw.items())[0:3])
# %%
# %%
slim_elements_order = slim_elements_df.sort_values('value',ascending=False)
top_value = slim_elements_order.set_index('second_name').T.to_dict('list')
print(top_value)
# %%
star_players = slim_elements_df.sort_values('total_points',ascending=False)
top_points = star_players.set_index('second_name').T.to_dict('list')
# %%
