import os
from itertools import groupby
import pandas as pd

dir_name = '../data/'

number_of_day = 4
time_per_frame = 4 # in second
number_of_frame_per_day = 24 * 60 * 60 / time_per_frame

def get_files():
  return sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                          os.listdir(dir_name) ) )

def get_bread(id):
  list_of_files = get_files()

  breads = [list(i) for j, i in groupby(list_of_files,
                    lambda a: a[0:3])]

  data = []
  for file in breads[id]:
    df = pd.read_csv(os.path.join(dir_name, file))
    df['filename'] = file
    data.append(df)
  return pd.concat(data, ignore_index=True)
  
def get_mice(id):
  list_of_files = get_files()
  df = pd.read_csv(os.path.join(dir_name, list_of_files[id]))
  df['filename'] = list_of_files[id]
  return df

def retrieve_day(df, day):
  '''
  @param df dataframe of a mice
  @param day day of the mice (1, 2, 3, 4)
  '''
  return df[(df.index / number_of_frame_per_day).astype(int) % number_of_day == day - 1]

def remove_day(df, day):
  '''
  @param df dataframe of a mice
  @param day day of the mice (1, 2, 3, 4)
  '''
  df = df.reset_index(drop=True)  # Reset the index before applying the time-based filter
  day_start = (day - 1) * number_of_frame_per_day
  day_end = day * number_of_frame_per_day
  return df[(df.index < day_start) | (df.index >= day_end)]

def remove_day_from_bread(bread_df, day):
  grouped = bread_df.groupby('filename')
  cleaned_data = pd.concat([remove_day(group, day) for name, group in grouped])
  return cleaned_data