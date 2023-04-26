import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents new Healthy Diner') 
streamlit.header('Menu')
streamlit.text('chepathi curry')
streamlit.text('any fruite')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#streamlit.header("Fruityvice Fruit Advice!")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())


#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)
#New Section to display fruityvice api response

#new api
'''streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input ('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json ())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error ()'''
#new api
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas. json_normalize(fruityvice_response.json ())
  return fruityvice_normalized
#New Section to display fruityvice api response
streamlit.header( 'Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input( 'What fruit would you like information about?')
  if not fruit_choice:
       streamlit.error ("Please select a fruit to get information.")
  else:
       back _from_function = get_fruityvice_data(fruit choice)
       streamlit.dataframe (back_from_function)
# don't run anything past here while we troubleshoot
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor ()
#my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur. fetchone ()
#streamlit.text ("the fruite load list")
#streamlit.text(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit. header ("The fruit load list count")
streamlit.dataframe (my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfurit')
streamlit.write('The user entered ', add_my_fruit)
streamlit.text('thanks for adding ' + add_my_fruit)
#This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
