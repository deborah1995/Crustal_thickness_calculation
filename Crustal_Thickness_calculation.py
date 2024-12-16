#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

file_path = 'Afonso_etal_GJI_2019_LithoRef18.xyz'

data = pd.read_csv(file_path, sep='\s+', comment='*', header=None, skiprows=30) 

data.columns = ['LONG', 'LAT', 'ELEVATION', 'MOHO', 'LAB', 'RHO_C', 'RHO_L', 'RHO_SL', 
                'BOTTOM', 'GEOID', 'FA', 'G_zz', 'G_xx', 'G_yy']

print(data.head())


# In[4]:


my_coordinates = [(-23.1492, -67.6585), (-23.1468, -67.4192), (-22.3307, -68.0118)]


# In[5]:


points = np.array(list(zip(data['LONG'], data['LAT'])))
values_elevation = data['ELEVATION'].values
values_moho = data['MOHO'].values


# In[6]:


# ELEVATION and MOHO interpolation
elevation_interp = griddata(points, values_elevation, my_coordinates, method='linear')
moho_interp = griddata(points, values_moho, my_coordinates, method='linear')


# In[7]:


# crustal thickness calculation
crustal_thickness = elevation_interp - moho_interp


# In[8]:


results = pd.DataFrame({
    'Longitude': [coord[0] for coord in my_coordinates],
    'Latitude': [coord[1] for coord in my_coordinates],
    'ELEVATION': elevation_interp,
    'MOHO': moho_interp,
    'Crustal_Thickness': crustal_thickness
})


# In[9]:


# Saving results as a CSV file
results.to_csv('crustal_thickness_results.csv', index=False)

print("Spessore crostale calcolato per le coordinate specifiche:")
print(results)


# In[ ]:





# In[ ]:




