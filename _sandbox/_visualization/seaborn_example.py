# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:27:34 2017

@author: sncc
"""
import os


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('C:\\Users\\sncc\\Dropbox\\workspace2\\net_con')
df = pd.read_excel('170613_re.xlsx')
df['kakaoF'] = pd.to_numeric(df['kakaoF'], errors='coerce')
df['one_to_one'] = pd.to_numeric(df['one_to_one'], errors = 'coerce')

############################fig1##############################
df2 = pd.read_csv('170606_fig.txt', sep="\t")
sns.set(color_codes = True)

plt.figure(figsize=(10, 8))
sns.distplot(df2['Duration'].dropna(), bins = 20, kde = False)
plt.xlabel('Duration', fontsize = 15)
plt.ylabel('Frequency', fontsize = 15)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
sns.plt.xlim(0,330)
plt.axvline(df2['Duration'].mean(), color = 'black', linestyle = 'dashed', linewidth = 1)
#sns.plt.fig
plt.savefig("fig1.png", dpi= 600, bbox_inches = 'tight')
############################fig3-1#############################

plt.figure(figsize=(10, 8))
sns.distplot(df['kakaoF'].dropna(), bins = 20, kde = False)
plt.xlabel('# of Kakao Friends', fontsize = 15)
plt.ylabel('Frequency', fontsize = 15)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.axvline(df['kakaoF'].mean(), color = 'black', linestyle = 'dashed', linewidth = 1)
plt.savefig("fig3-1.png", dpi = 600, bbox_inches = 'tight')
##sns.displot(df['])2d

############################fig3-2#############################
plt.figure(figsize=(10, 8))
sns.distplot(df['one_to_one'].dropna(), bins = 20 ,kde = False)
plt.xlabel('# of two-person chatrooms', fontsize = 15)
plt.ylabel('Frequency', fontsize = 15)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.axvline(df['one_to_one'].mean(), color = 'black', linestyle = 'dashed', linewidth = 1)
plt.savefig("fig3-2.png", dpi = 600, bbox_inches = 'tight')

############################fig4#############################
plt.figure(figsize=(10,8))
sns.distplot(df['overlap'], bins = 15, kde = False)
plt.xlabel("Overlap ratio", fontsize = 15)
plt.ylabel("Frequency", fontsize = 15)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.axvline(df['overlap'].mean(), color = 'black', linestyle = 'dashed', linewidth = 1)
plt.savefig("fig4.png", dpi= 600, bbox_inches = 'tight')


############################fig5#############################

plt.figure(figsize=(8,6))
sns.regplot(x ='fig5', y = 'overlap', data = df)
sns.plt.xlim(-0.05,1.05)
sns.plt.ylim(-0.05,1.05)
plt.xlabel('The ratio of strong tie to non-family member', fontsize = 15)
plt.ylabel('Overlap ratio', fontsize= 15)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.savefig("fig5-1.png", dpi = 600, bbox_inches = 'tight')


plt.figure(figsize=(8,6))
sns.regplot(x ='one_to_one', y = 'overlap', data = df, color = sns.xkcd_rgb["pale red"])
sns.plt.xlim(-3,90)
sns.plt.ylim(-0.05, 1.05)
plt.xlabel('# of two-person chatrooms', fontsize = 15)
plt.ylabel('Overlap ratio', fontsize= 15)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.savefig("fig5-2.png", dpi = 600, bbox_inches = 'tight')


############################fig5#############################
df_fig2 = pd.read_excel('for_fig2.xlsx')
sns.set()
f, ax = plt.subplots(figsize = (10,5))
sns.barplot(x = 'above', y = 'Frequency', data = df_fig2, label = 'above', color = 'b' , orient= 'h')
sns.set_color_codes("muted")
sns.barplot(x = 'under', y = 'Frequency', data=df_fig2,
            label="under", color="blue", orient = 'h')
plt.xlabel('')
plt.ylabel('')
#plt.legend(loc='upper right')
plt.xlim(-45,45)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are 