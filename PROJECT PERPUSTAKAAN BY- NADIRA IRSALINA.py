#!/usr/bin/env python
# coding: utf-8

# ## PROYEK PERPUSTAKAAN
# 
# ## VLP4
# ## NADIRA IRSALINA DBA2134265

# 1. Variabel pada Python
# 2. Operator pada Python
# 3. Tipe Data pada Python

# In[32]:


#Inisialisasi
Nama_buku_1="Fisika"
Nama_buku_2="Kimia"
Nama_buku_3="Biologi"
durasi=3


# In[33]:


type(Nama_buku_1),type(Nama_buku_2),type(Nama_buku_3), type(durasi)


# In[34]:


kode_buku_1="PS_001"
kode_buku_2="PS_002"
kode_buku_3="PS_003"


# In[35]:


N_buku_1=N_buku_2=N_buku_3=10


# In[36]:



type(N_buku_1)


# ## VLP6

# 1. list
# 2. tuple
# 3. dictionary
# 

# In[37]:


Nama_buku=(Nama_buku_1,Nama_buku_2,Nama_buku_3)
Kode_buku=[kode_buku_1,kode_buku_2,kode_buku_3]
N_buku=[N_buku_1, N_buku_2, N_buku_3]


# In[38]:


type(Nama_buku), type(Kode_buku), type(N_buku)


# In[39]:


pustaka={"Nama":Nama_buku,
 "Kode":Kode_buku,
 "Jumlah":N_buku}


# In[40]:


type(pustaka)


# In[41]:


pustaka


# Penambahan buku
# 

# In[42]:


Nama_buku=[Nama_buku_1,Nama_buku_2,Nama_buku_3]
pustaka={"Nama":Nama_buku,
        "Kode":Kode_buku,
        "Jumlah":N_buku}
pustaka


# In[43]:


pustaka['Nama'].append('Seni')
pustaka['Kode'].append('PS_004')
pustaka['Jumlah'].append(15)
print("Buku {} dengan jumlah {}".format(pustaka["Nama"][-1],
                                        pustaka['Jumlah'][-1]))


# In[44]:


pustaka


# ## VLP8

# 1. Denda harga sewa perhari
# 2. Bila tersedia >1, boleh pinjam; else tidak boleh

# In[45]:


print("Buku yang tersedia:")
print("Nama Buku\t Kode Buku\t Jumlah")
for i in range(len(pustaka['Nama'])):
    print("Buku {}\t kode {}\t {}".format(
        pustaka['Nama'][i],
        pustaka['Kode'][i],
        pustaka['Jumlah'][i]))


# In[46]:


print("Form Peminjaman")
varNama=str(input("Nama Peminjam ="))
varBuku=str(input("Kode Buku= "))
for i in range(len(pustaka['Kode'])):
    if varBuku==pustaka['Kode'][i] and pustaka['Jumlah'][i]>1:
        print("Bisa pinjam".format(varNama))
        print("Durasi waktu pinjam {} hari".format(durasi))
        pustaka['Jumlah'][i]-=1
    elif i==len(pustaka['Kode'])-1:
        print("Tidak bisa dipinjam")


# In[47]:


pustaka


# In[48]:


print("Form Pengembalian")
varNama=str(input("Nama Peminjam\t="))
varBuku=str(input("Kode Buku\t="))
varHari=int(input("Jumlah Hari\t="))
for i in range(len(pustaka['Kode'])) :
    if varBuku==pustaka['Kode'][i] :
        if varHari>=durasi:
            denda=(varHari-durasi)*1000
            print("Terima kasih, {}\nDenda sebesar Rp.{}".format(varNama,denda))
            pustaka['Jumlah'][i]+=1
            break
        else:
            print("Terima kasih,{}".format(varNama))
            pustaka['Jumlah'][i]+=1
            break
    elif i==len(pustaka['Kode'])-1:
        print("Salah kode")


# In[49]:


pustaka


# ## VLP10

# 1. Fungsi Peminjaman
# 2. Fungsi Pengembalian
# 3. Fungsi Data Terakhir

# In[50]:


def Data_terakhir():
    print("Buku yang tersedia:")
    print("Nama Buku\t Kode Buku\t Jumlah")
    for i in range(len(pustaka['Nama'])):
        print("Buku {}\t kode {}\t {}".format(
            pustaka['Nama'][i],
            pustaka['Kode'][i],
            pustaka['Jumlah'][i]))
            
            


# In[51]:


Data_terakhir()


# In[52]:


def peminjaman():
    print("Form Peminjaman")
    varNama=str(input("Nama Peminjam ="))
    varBuku=str(input("Kode Buku= "))
    for i in range(len(pustaka['Kode'])):
        if varBuku==pustaka['Kode'][i] and pustaka['Jumlah'][i]>1:
            print("Bisa pinjam".format(varNama))
            print("Durasi waktu pinjam {} hari".format(durasi))
            pustaka['Jumlah'][i]-=1
            break
        elif i==len(pustaka['Kode'])-1:
            print("Tidak bisa dipinjam")


# In[54]:


peminjaman()


# In[55]:


def pengembalian(pustaka=pustaka):
    print("Form Pengembalian")
    varNama=str(input("Nama Peminjam\t="))
    varBuku=str(input("Kode Buku\t="))
    varHari=int(input("Jumlah Hari\t="))
    for i in range(len(pustaka['Kode'])):
        if varBuku==pustaka['Kode'][i]:
            if varHari>=durasi:
                denda=(varHari-durasi)*1000
                print("Terima kasih, {}\nDenda sebesar Rp.{}".format(varNama,denda))
                pustaka['Jumlah'][i]+=1
                break
            else:
                print("Terima kasih,{}".format(varNama,denda))
                pustaka['Jumlah'][i]+=1
                break
        elif i==len(pustaka['Kode'])-1:
            print("Salah kode")


# In[56]:


pengembalian()


# In[57]:


def tambah_buku(varBuku,varKode,varJumlah):
    for i in range(len(pustaka['Kode'])):
        if varKode==pustaka['Kode'][i]:
            pustaka['Jumlah'][i]+=varJumlah
            print("Buku {} dengan Jumlah {}".format(pustaka["Nama"][i],
                                                    pustaka['Jumlah'][i]))
            
            break
    else:
        pustaka['Nama'].append(varBuku)
        pustaka['Kode'].append(varKode)
        pustaka['Jumlah'].append(varJumlah)
    
    print("Buku Baru {} dengan Jumlah {}".format(pustaka["Nama"][-1],
                                                    pustaka['Jumlah'][-1]))                 


# In[58]:


Data_terakhir()


# In[ ]:


Judul="Seni"
Kode="PS_004"
Jumlah=7
tambah_buku(Judul,Kode,Jumlah)


# In[59]:


Data_terakhir()


# In[60]:


Judul="Sastra"
Kode="PS_005"
Jumlah=5
tambah_buku(Judul,Kode,Jumlah)


# In[61]:


Data_terakhir()


# ## VLP12

# In[62]:


import pandas as pd


# In[63]:


df=pd.DataFrame(pustaka)


# In[64]:


df


# In[65]:


len(df)


# In[66]:


def peminjaman_df(durasi=durasi):
    print("Form Peminjaman")
    varNama=str(input("Nama Peminjam ="))
    varBuku=str(input("Kode Buku= "))
    for i in range(len(df)):
        if (varBuku==df['Kode'].iloc[i] and df['Jumlah'].iloc[i]>1):
            print("Bisa pinjam".format(varNama))
            print("Durasi waktu pinjam {} hari".format(durasi))
            df.at[i,'Jumlah']-=1
            return df
            break
        elif i==len(df) :
            print("Tidak bisa dipinjam")


# In[67]:


def pengembalian_df(durasi=durasi):
    print("Form Pengembalian")
    varNama=str(input("Nama Peminjam\t="))
    varBuku=str(input("Kode Buku\t="))
    varHari=int(input("Jumlah Hari\t="))
    for i in range(len(df)):
        if varBuku==df['Kode'].iloc[i]:
            if varHari>=durasi:
                denda=(varHari-durasi)*1000
                print("Terima kasih, {}\nDenda sebesar Rp.{}".format(varNama,denda))
                df.at['Jumlah'][i]+=1
                return df
                break
            else:
                print("Terima kasih,{}".format(varNama))
                varBar=df['Jumlah'].iloc[i]
                df.at[i,'Jumlah'][i]+=1
                return df
                break
        elif i==len(df)-1:
            print("Salah kode")


# In[68]:


def tambah_buku(varBuku,varKode,varJumlah):
    for i in range(len(pustaka['Kode'])):
        if varKode==df['Kode'][i]:
            df.at[i,'Jumlah'][i]+=varJumlah
            return df
            print("Buku {} dengan Jumlah {}".format(df["Nama"].iloc[i],
                                                    df['Jumlah'].iloc[i]))
            
            break
    else:
        var1={"Nama":varBuku,
              "Kode":varKode,
              "Jumlah":varJumlah}
    df=df.append(var1, ignore_index=True)
    print("Buku Baru {} dengan Jumlah {}".format(df["Nama"].iloc[-1],
                                                    df['Jumlah'].iloc[-1]))
    
    return df


# In[69]:


df


# In[70]:


df=peminjaman_df()


# In[71]:


df


# In[72]:


Judul="Astronomi"
Kode="PS_006"
Jumlah=5

df=tambah_buku_df(Judul,Kode,Jumlah)


# In[77]:


def tambah_buku_df(varBuku,varKode,varJumlah,df=df):
    for i in range(len(df)):
        if varKode==df['Kode'].iloc[i]:
            df.at[i,'Jumlah']+=varJumlah
            return df
            print("Buku {} dengan Jumlah {}".format(df["Nama"].iloc[i],
                                                    df['Jumlah'].iloc[i]))
            break
    else:
        var1={"Nama":varBuku,
              "Kode":varKode,
              "Jumlah":varJumlah}
    df=df.append(var1, ignore_index=True)
    print("Buku Baru {} dengan Jumlah {}".format(df["Nama"].iloc[-1],
                                                    df['Jumlah'].iloc[-1]))
    
    return df


# In[78]:


Judul="Astronomi"
Kode="PS_006"
Jumlah=5
df=tambah_buku_df(Judul,Kode,Jumlah)


# In[83]:


df


# ## VLP14

# 1. Alokasi Kolom baru
# 2. Bar
# 3. Pie
# 

# In[81]:


import numpy as np


# In[82]:


import matplotlib.pyplot as plt


# In[84]:


df['Pinjam']=np.random.randint(1,7)
df


# In[85]:


df['Pinjam']=np.random.randint(1,7,len(df))
df


# In[89]:


def peminjaman_df(durasi=durasi):
    print("Form Peminjaman")
    varNama=str(input("Nama Peminjam ="))
    varBuku=str(input("Kode Buku= "))
    for i in range(len(df)):
        if (varBuku==df['Kode'].iloc[i] and df['Jumlah'][i]>1):
            print("Bisa pinjam {}".format(varNama))
            print("Durasi waktu pinjam {} hari".format(durasi))
            df.at[i,'Jumlah']-=1
            df.at[i,'Pinjam']+=1
            return df
            break
        elif i==len(df)-1:
            print("Tidak bisa dipinjam")
        


# In[101]:


def pengembalian_df(durasi=durasi):
    print("Form Pengembalian")
    varNama=str(input("Nama Peminjam\t="))
    varBuku=str(input("Kode Buku\t="))
    varHari=int(input("Jumlah Hari\t="))
    for i in range(len(df)):
        if varBuku==df['Kode'].iloc[i]:
            if varHari>=durasi:
                denda=(varHari-durasi)*1000
                print("Terima kasih, {}\nDenda sebesar Rp.{}".format(varNama,denda))
                df.at[i,'Jumlah']+=1
                df.at[i,'Pinjam']-=1
                return df
                break
            else:
                print("Terima kasih,{}".format(varNama))
                varBar=df['Jumlah'].iloc[i]
                df.at[i,'Jumlah']+=1
                df.at[i,'Pinjam']-=1
                return df
                break
        elif i==len(df)-1:
            print("Salah kode")  


# In[102]:


df


# In[103]:


df=peminjaman_df()


# In[104]:


df


# In[105]:


df=pengembalian_df() 


# In[106]:


df


# In[120]:


plt.title("Ketersediaan Buku")
pjgLabel=np.arange(len(df))
lbr=0.5
varLabel=df['Nama'].values
varJumlah=df['Jumlah'].values
varPinjam=df['Pinjam'].values
plt.bar(pjgLabel,varJumlah, color='gold',
        width=lbr, label="Jumlah")
plt.bar(pjgLabel+lbr,varPinjam, color='red',
        width=lbr, label="Pinjam")
plt.legend(loc='best')
plt.show()


# In[121]:


plt.title("Persentase Ketersediaan Buku")
plt.pie(varJumlah,labels=varLabel, autopct='%1.2f%%',
        shadow=True)
plt.show()


# In[122]:


plt.title("Persentase Peminjaman Buku")
plt.pie(varJumlah,labels=varLabel, autopct='%1.2f%%')
plt.show()


# ### SELESAI

# In[ ]:




