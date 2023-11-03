#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as ny
import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import holoviews as hv
hv.extension('bokeh')


# In[2]:


data = [
    ['CARD_PAYMENT', 'Current', '2023-01-26 22:02:47', '2023-01-27 10:10:12', 'Ikea Stores 6601', -6.35, 0, 'INR', 'COMPLETED', 521.07],
    ['CARD_PAYMENT', 'Current', '2023-01-26 16:13:50', '2023-01-27 11:50:32', 'Zettle_*donovan?s Bake', -2.5, 0, 'INR', 'COMPLETED', 518.57],
    ['CARD_PAYMENT', 'Current', '2023-01-26 08:26:35', '2023-01-27 13:42:55', 'apple.com/bill', -3.99, 0, 'INR', 'COMPLETED', 514.58],
    ['CARD_PAYMENT', 'Current', '2023-01-27 13:16:59', '2023-01-28 09:59:20', 'Ikea Stores 6601', -4.85, 0, 'INR', 'COMPLETED', 509.73],
    ['CARD_PAYMENT', 'Current', '2023-01-27 10:43:22', '2023-01-28 11:48:36', 'Zettle_*the Good Eatin', -3.3, 0, 'INR', 'COMPLETED', 506.43],
    ['CARD_PAYMENT', 'Current', '2023-01-27 19:07:07', '2023-01-28 15:51:42', 'Toogoodtog Mzs3m03xcn9', -5, 0, 'INR', 'COMPLETED', 501.43],
    ['CARD_PAYMENT', 'Current', '2023-01-28 01:14:16', '2023-01-29 08:55:25', 'Fisco Bar', -21, 0, 'INR', 'COMPLETED', 480.43],
    ['CARD_PAYMENT', 'Current', '2023-01-28 16:26:00', '2023-01-29 09:41:04', 'Amznmktplace', -8.99, 0, 'INR', 'COMPLETED', 471.44],
    ['CARD_PAYMENT', 'Current', '2023-01-28 19:59:36', '2023-01-29 09:49:29', 'Ikea Stores 6601', -8.65, 0, 'INR', 'COMPLETED', 462.79],
    ['CARD_PAYMENT', 'Current', '2023-01-27 22:59:58', '2023-01-29 10:08:56', 'Zudio 40', -12.6, 0, 'INR', 'COMPLETED', 450.19],
    ['CARD_PAYMENT', 'Current', '2023-01-27 22:06:03', '2023-01-29 10:08:56', 'Zudio 40', -6.1, 0, 'INR', 'COMPLETED', 444.09],
    ['CARD_PAYMENT', 'Current', '2023-01-29 02:39:46', '2023-01-29 10:55:55', 'Tfl Travel Charge', -4.25, 0, 'INR', 'COMPLETED', 439.84],
    ['CARD_PAYMENT', 'Current', '2023-01-28 15:06:44', '2023-01-29 11:31:51', 'Sq *lavelle Coffee Limite', -3.2, 0, 'INR', 'COMPLETED', 436.64],
    ['CARD_PAYMENT', 'Current', '2023-01-29 15:08:04', '2023-01-31 14:06:07', 'Tubebuddycom*', -2.43, 0.02, 'INR', 'COMPLETED', 451.69],
    ['CARD_PAYMENT', 'Current', '2023-01-29 15:11:03', '2023-01-31 14:45:55', 'Sp Blomma Beauty', -35, 0, 'INR', 'COMPLETED', 416.69],
    ['CARD_PAYMENT', 'Current', '2023-01-29 20:03:55', '2023-01-31 15:11:28', 'Uber* Trip', -13.46, 0,'INR', 'COMPLETED', 403.23],
    ['CARD_PAYMENT', 'Current', '2023-01-29 14:31:09', '2023-01-31 17:29:48', 'Caravan', -27.67, 0, 'INR', 'COMPLETED', 375.56],
    ['CARD_PAYMENT', 'Current', '2023-01-30 01:57:58', '2023-01-31 17:41:29', 'Tfl Travel Charge', -4.25, 0, 'INR', 'COMPLETED', 371.31],
    ['CARD_PAYMENT', 'Current', '2023-01-31 02:36:53', '2023-01-31 18:03:14', 'Tfl Travel Charge', -1.65, 0, 'INR', 'COMPLETED', 369.66],
    ['CARD_PAYMENT', 'Current', '2023-01-29 19:13:59', '2023-01-31 18:46:41', 'The Green Kitchen Hotel', -3.6, 0, 'INR', 'COMPLETED', 366.06],
    ['CARD_PAYMENT', 'Current', '2023-01-30 19:03:58', '2023-01-31 19:00:20', 'Ikea Stores 6601', -4.25, 0, 'INR', 'COMPLETED', 361.81],
    ['CARD_PAYMENT', 'Current', '2023-01-30 13:41:48', '2023-01-31 19:32:36', 'Lidl Mumbai', -8.12, 0, 'INR', 'COMPLETED', 343.69],
    ['CARD_PAYMENT', 'Current', '2023-01-30 11:55:40', '2023-01-31 19:55:25', 'E5 Bakehouse Canning T', -12.36, 0, 'INR', 'COMPLETED', 331.33],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Amznmktplace', -17.07, 0, 'INR', 'COMPLETED', 555.43],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Starbucks', -3.95, 0, 'INR', 'COMPLETED', 551.48],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Tfl Travel Charge', -2.6, 0, 'INR', 'COMPLETED', 548.88],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Mini Store', -5, 0, 'INR', 'COMPLETED', 543.88],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'cm.com', -253, 0, 'INR', 'COMPLETED', 290.88],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Dakshak100', -12.25, 0, 'INR', 'COMPLETED', 278.63],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Ubr* Pending.uber.com', -13.66, 0, 'INR', 'COMPLETED', 264.97],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Ubr* Pending.uber.com', -7.03, 0, 'INR', 'COMPLETED', 257.94],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Starbucks', -3.9, 0, 'INR', 'COMPLETED', 254.04]
]

columns = ['Type', 'Product', 'Started Date', 'Completed Date', 'Description', 'Amount', 'Fee', 'Currency', 'State', 'Balance']

df = pd.DataFrame(data=data, columns=columns)


# In[3]:


df


# In[4]:


df = df[['Completed Date', 'Description', 'Amount']] 
df['Description'] = df['Description'].map(str.lower) 
df = df.rename(columns={'Completed Date': 'Date'})   
df['Category'] = 'unassigned'                        
df.head()


# In[5]:


df['Category'] = ny.where(df['Description'].str.contains(
    'cash at tesco old st h exp|boots|royal'), 
    'Self-Care', df['Category'] )
    

df['Category'] = ny.where(df['Description'].str.contains(
    'car rental'), 
    'Fines', df['Category'] )
    

df['Category'] = ny.where(df['Description'].str.contains(
    'tubebuddy|itunes|dario|calendly|canva|epidemic|upwork|lada'), 
    'Atharva', df['Category'] )
    

df['Category'] = ny.where(df['Description'].str.contains(
    'lavelle|hart|starbucks|barista|new road|mama shelter'), 
    'Coffee', df['Category'] )
    
    
df['Category'] = ny.where(df['Description'].str.contains(
    'islington|at camden town'), 
    'Shopping', df['Category'] )
    

df['Category'] = ny.where(df['Description'].str.contains(
    'bakehouse|zettle|caravan|kod|eating|kitchen|restaurant|dakshak'), 
    'Restaurants', df['Category'] )
        
    
df['Category'] = ny.where(df['Description'].str.contains(
    'fisco|zudio|oshveda|egg|francesco|budgens whitechapel'), 
    'Entertainment', df['Category'] )
    
    
df['Category'] = ny.where(df['Description'].str.contains(
    'gucci|blomma'), 
    'Gifts', df['Category'] )
    
    
df['Category'] = ny.where(df['Description'].str.contains(
    'apple|snappy|exchanged to usd'), 
    'Services', df['Category'] )
    
    
df['Category'] = ny.where(df['Description'].str.contains(
    'from|paypal|amznmktplace|starnow|refund|giffgaff|backstage|hectagon|tower hamlets bc|sweet suites|temporary hold|cm.com'), 
    'Excluded', df['Category'] )


df['Category'] = ny.where(df['Description'].str.contains(
    'ikea|sainsbury|asda|lidl|toogoodtog|nisa|market|mini store'), 
    'Groceries', df['Category'] )

    
df['Category'] = ny.where(df['Description'].str.contains(
    'uber|zipcar|bird|tfl|Ewa'), 
    'Transport', df['Category'] )
    
    
df['Category'] = ny.where(df['Description'].str.contains(
    'ryanair|easyjet|airways'), 
    'Travel', df['Category'] )

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
    
pd.options.display.max_rows = 999
df.head(200)


# In[8]:


unassigned = df.loc[df['Category'] == 'unassigned']
unassigned


# In[12]:


latest_month = df['Month'].max()
latest_year = df['Year'].max()
previous_month_expenses = df[(df['Month'] == latest_month) & (df['Year'] == latest_year)]


# In[13]:


previous_month_expenses = previous_month_expenses.groupby('Category')['Amount'].sum().reset_index()

previous_month_expenses['Amount']=previous_month_expenses['Amount'].astype('str')
previous_month_expenses['Amount']=previous_month_expenses['Amount'].str.replace('-','')
previous_month_expenses['Amount']=previous_month_expenses['Amount'].astype('float')        

previous_month_expenses = previous_month_expenses[previous_month_expenses["Category"].str.contains("Excluded|unassigned") == False] 
previous_month_expenses = previous_month_expenses.sort_values(by='Amount', ascending=False)    
previous_month_expenses['Amount'] = previous_month_expenses['Amount'].round().astype(int)      

previous_month_expenses


# In[15]:


previous_month_expenses_tot = last_month_expenses['Amount'].sum()
previous_month_expenses_tot


# In[17]:


def calculate_difference(event):
    income = float(income_widget.value)
    recurring_expenses = float(recurring_expenses_widget.value)
    monthly_expenses = float(monthly_expenses_widget.value)
    difference = income - recurring_expenses - monthly_expenses
    difference_widget.value = str(difference)

income_widget = pn.widgets.TextInput(name="Income", value="0")
recurring_expenses_widget = pn.widgets.TextInput(name="Recurring Expenses", value="0")
monthly_expenses_widget = pn.widgets.TextInput(name="Non-Recurring Expenses", value=str(previous_month_expenses_tot))
difference_widget = pn.widgets.TextInput(name="Previous Month's Savings", value="0")
income_widget.param.watch(calculate_difference, "value")
recurring_expenses_widget.param.watch(calculate_difference, "value")
monthly_expenses_widget.param.watch(calculate_difference, "value")


# In[18]:


previous_month_expenses_chart = previous_month_expenses.hvplot.bar(
    x='Category', 
    y='Amount', 
    height=250, 
    width=550, 
    title="Previous Month Expenses",
    ylim=(0, 30))

previous_month_expenses_chart


# In[19]:


df['Date'] = pd.to_datetime(df['Date'])            
df['Month-Year'] = df['Date'].dt.to_period('M')  
monthly_expenses_trend_by_category = df.groupby(['Month-Year', 'Category'])['Amount'].sum().reset_index()

monthly_expenses_trend_by_category['Amount']=monthly_expenses_trend_by_category['Amount'].astype('str')
monthly_expenses_trend_by_category['Amount']=monthly_expenses_trend_by_category['Amount'].str.replace('-','')
monthly_expenses_trend_by_category['Amount']=monthly_expenses_trend_by_category['Amount'].astype('float')
monthly_expenses_trend_by_category= monthly_expenses_trend_by_category[monthly_expenses_trend_by_category["Category"].str.contains("Excluded") == False]

monthly_expenses_trend_by_category = monthly_expenses_trend_by_category.sort_values(by='Amount', ascending=False)
monthly_expenses_trend_by_category['Amount'] = monthly_expenses_trend_by_category['Amount'].round().astype(int)
monthly_expenses_trend_by_category['Month-Year'] = monthly_expenses_trend_by_category['Month-Year'].astype(str)
monthly_expenses_trend_by_category = monthly_expenses_trend_by_category.rename(columns={'Amount': 'Amount '})

monthly_expenses_trend_by_category


# In[20]:


select_category1 = pn.widgets.Select(name='Select Category', options=[
    'All',
    'Self-Care',
    'Fines',
    'Atharva',
    'Coffee',
    'Groceries',
    'Shopping',
    'Restaurants',
    'Transport',
    'Travel',
    'Entertainment',
    'Gifts',
    'Services',
])

select_category1


# In[21]:


def plot_expenses(category):
    if category == 'All':
        plot_df = monthly_expenses_trend_by_category.groupby('Month-Year').sum()
    else:
        plot_df = monthly_expenses_trend_by_category[monthly_expenses_trend_by_category['Category'] == category].groupby('Month-Year').sum()
    plot = plot_df.hvplot.bar(x='Month-Year', y='Amount ')
    return plot
@pn.depends(select_category1.param.value)
def update_plot(category):
    plot = plot_expenses(category)
    return plot


# In[22]:


monthly_expenses_trend_by_category_chart = pn.Row(select_category1, update_plot)
monthly_expenses_trend_by_category_chart[1].width = 600
monthly_expenses_trend_by_category_chart


# In[23]:


df = df[['Date', 'Category', 'Description', 'Amount']]
df['Amount']=df['Amount'].astype('str')
df['Amount']=df['Amount'].str.replace('-','')
df['Amount']=df['Amount'].astype('float')        

df = df[df["Category"].str.contains("Excluded") == False]    
df['Amount'] = df['Amount'].round().astype(int) 
df


# In[24]:


def filter_df(category):
    if category == 'All':
        return df
    return df[df['Category'] == category]


# In[25]:


summary_table = pn.widgets.DataFrame(filter_df('All'), height = 300,width=400)


# In[26]:


def update_summary_table(event):
    summary_table.value = filter_df(event.new)


# In[27]:


select_category1.param.watch(update_summary_table, 'value')


# In[28]:


template = pn.template.FastListTemplate(
    title="FinMaster",
    sidebar=[
        pn.pane.Markdown("## **Managing money is the key,So learn it and be rich**"),
        pn.pane.PNG('https://static.vecteezy.com/system/resources/thumbnails/024/043/947/small/money-bag-clipart-transparent-background-free-png.png', sizing_mode='scale_both'),
        pn.pane.Markdown(""),
        pn.pane.Markdown(""),
        select_category1
    ],
    main=[
        pn.Row(income_widget, recurring_expenses_widget, monthly_expenses_widget, difference_widget, width=950),
        pn.GridBox(
            monthly_expenses_trend_by_category_chart[1],
            summary_table,
            ncols=2,
            width=500,  
            align='start',
            sizing_mode='stretch_width'
        ),
        pn.Row(previous_month_expenses_chart, height=240)
    ]
)
template.show()


# In[ ]:





# In[ ]:




