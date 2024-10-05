df = pd.read_csv('country_vaccinations.csv')
# print(df.head())
df['vaccination_rate'] =(((df['total_vaccinations']-df['people_fully_vaccinated'])*100)/(df['total_vaccinations']))
# print(df)
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(df['daily_vaccinations'].mean())
# print(df)
df = df.drop('source_name', axis=1)
# df = df.dropna()
# print(df)
df['total_vaccinations'] = df['total_vaccinations'].fillna(df['total_vaccinations'].mean())
df_sorted = df.sort_values(by='total_vaccinations', ascending=True)
# print(df_sorted.head(20))
df =df_sorted.rename(columns={'iso_code':'country_code'})
df.index = range(1,len(df)+1)
#print(df.head())
count_na = df.isna().sum()
print(count_na)
df['people_fully_vaccinated']=df['people_fully_vaccinated'].fillna(0)
df = df.dropna(subset=['total_vaccinations'])
df['vaccines'].replace('Moderna, Pfizer/BioNTech', 'mRNA vaccines')
df.loc[df['daily_vaccinations'] < 0, 'daily_vaccinations'] = 0
print(df.head(20))

# #####################################################################
# OUTPUT
# country                                   0
# country_code                              0
# date                                      0
# total_vaccinations                        0
# people_vaccinated                      4885
# people_fully_vaccinated                6557
# daily_vaccinations_raw                 5303
# daily_vaccinations                        0
# total_vaccinations_per_hundred         4257
# people_vaccinated_per_hundred          4885
# people_fully_vaccinated_per_hundred    6557
# daily_vaccinations_per_million          194
# vaccines                                  0
# source_website                            0
# vaccination_rate                       6558
# dtype: int64
#                   country country_code        date  total_vaccinations  \
# 1             Afghanistan          AFG  2021-02-22                 0.0   
# 2               Australia          AUS  2021-02-20                 0.0   
# 3               Australia          AUS  2021-02-21                 0.0   
# 4                Slovakia          SVK  2021-01-04                 0.0   
# 5            Sierra Leone          SLE  2021-03-14                 0.0   
# 6              Seychelles          SYC  2021-01-09                 0.0   
# 7                 Senegal          SEN  2021-02-22                 0.0   
# 8              Azerbaijan          AZE  2021-01-17                 0.0   
# 9   Sao Tome and Principe          STP  2021-03-15                 0.0   
# 10            Saint Lucia          LCA  2021-02-16                 0.0   
# 11  Saint Kitts and Nevis          KNA  2021-02-22                 0.0   
# 12                 Rwanda          RWA  2021-02-15                 0.0   
# 13                  Qatar          QAT  2020-12-22                 0.0   
# 14            Philippines          PHL  2021-02-28                 0.0   
# 15             Bangladesh          BGD  2021-01-26                 0.0   
# 16               Paraguay          PRY  2021-02-21                 0.0   
# 17       Papua New Guinea          PNG  2021-03-29                 0.0   
# 18                 Panama          PAN  2021-01-19                 0.0   
# 19                Belarus          BLR  2020-12-28                 0.0   
# 20               Pakistan          PAK  2021-02-02                 0.0   

#     people_vaccinated  people_fully_vaccinated  daily_vaccinations_raw  \
# 1                 0.0                      0.0                     NaN   
# 2                 0.0                      0.0                     0.0   
# 3                 0.0                      0.0                     0.0   
# 4                 0.0                      0.0                     NaN   
# 5                 0.0                      0.0                     NaN   
# 6                 0.0                      0.0                     NaN   
# 7                 0.0                      0.0                     NaN   
# 8                 0.0                      0.0                     NaN   
# 9                 0.0                      0.0                     NaN   
# 10                0.0                      0.0                     NaN   
# 11                0.0                      0.0                     NaN   
# 12                0.0                      0.0                     NaN   
# 13                NaN                      0.0                     NaN   
# 14                0.0                      0.0                     NaN   
# 15                0.0                      0.0                     NaN   
# 16                0.0                      0.0                     NaN   
# 17                0.0                      0.0                     NaN   
# 18                NaN                      0.0                     NaN   
# 19                0.0                      0.0                     NaN   
# 20                0.0                      0.0                     NaN   

#     daily_vaccinations  total_vaccinations_per_hundred  \
# 1         68914.480341                             0.0   
# 2             0.000000                             0.0   
# 3             0.000000                             0.0   
# 4         68914.480341                             0.0   
# 5         68914.480341                             0.0   
# 6         68914.480341                             0.0   
# 7         68914.480341                             0.0   
# 8         68914.480341                             0.0   
# 9         68914.480341                             0.0   
# 10        68914.480341                             0.0   
# 11        68914.480341                             0.0   
# 12        68914.480341                             0.0   
# 13        68914.480341                             0.0   
# 14        68914.480341                             0.0   
# 15        68914.480341                             0.0   
# 16        68914.480341                             0.0   
# 17        68914.480341                             0.0   
# 18        68914.480341                             0.0   
# 19        68914.480341                             0.0   
# 20        68914.480341                             0.0   

#     people_vaccinated_per_hundred  people_fully_vaccinated_per_hundred  \
# 1                             0.0                                  NaN   
# 2                             0.0                                  NaN   
# 3                             0.0                                  NaN   
# 4                             0.0                                  NaN   
# 5                             0.0                                  NaN   
# 6                             0.0                                  NaN   
# 7                             0.0                                  NaN   
# 8                             0.0                                  NaN   
# 9                             0.0                                  NaN   
# 10                            0.0                                  NaN   
# 11                            0.0                                  NaN   
# 12                            0.0                                  NaN   
# 13                            NaN                                  NaN   
# 14                            0.0                                  NaN   
# 15                            0.0                                  NaN   
# 16                            0.0                                  NaN   
# 17                            0.0                                  NaN   
# 18                            NaN                                  NaN   
# 19                            0.0                                  NaN   
# 20                            0.0                                  NaN   

#     daily_vaccinations_per_million  \
# 1                              NaN   
# 2                              0.0   
# 3                              0.0   
# 4                              NaN   
# 5                              NaN   
# 6                              NaN   
# 7                              NaN   
# 8                              NaN   
# 9                              NaN   
# 10                             NaN   
# 11                             NaN   
# 12                             NaN   
# 13                             NaN   
# 14                             NaN   
# 15                             NaN   
# 16                             NaN   
# 17                             NaN   
# 18                             NaN   
# 19                             NaN   
# 20                             NaN   

#                                             vaccines  \
# 1                                 Oxford/AstraZeneca   
# 2                Oxford/AstraZeneca, Pfizer/BioNTech   
# 3                Oxford/AstraZeneca, Pfizer/BioNTech   
# 4                                    Pfizer/BioNTech   
# 5                                 Oxford/AstraZeneca   
# 6              Oxford/AstraZeneca, Sinopharm/Beijing   
# 7                                  Sinopharm/Beijing   
# 8                                            Sinovac   
# 9                                 Oxford/AstraZeneca   
# 10                                Oxford/AstraZeneca   
# 11                                Oxford/AstraZeneca   
# 12      Moderna, Oxford/AstraZeneca, Pfizer/BioNTech   
# 13                                   Pfizer/BioNTech   
# 14                       Oxford/AstraZeneca, Sinovac   
# 15                                Oxford/AstraZeneca   
# 16                                         Sputnik V   
# 17                                Oxford/AstraZeneca   
# 18                                   Pfizer/BioNTech   
# 19                                         Sputnik V   
# 20  Oxford/AstraZeneca, Sinopharm/Beijing, Sputnik V   

#                                        source_website  vaccination_rate  
# 1   http://www.xinhuanet.com/english/asiapacific/2...               NaN  
# 2               https://covidlive.com.au/vaccinations               NaN  
# 3               https://covidlive.com.au/vaccinations               NaN  
# 4   https://github.com/Institut-Zdravotnych-Analyz...               NaN  
# 5   https://www.facebook.com/mohsict/posts/1364398...               NaN  
# 6   https://www.facebook.com/mohseychellesofficial...               NaN  
# 7   https://twitter.com/MinisteredelaS1/status/138...               NaN  
# 8              https://koronavirusinfo.az/az/post/753               NaN  
# 9   https://www.facebook.com/MSaudeSTeP/photos/pcb...               NaN  
# 10                    https://www.covid19response.lc/               NaN  
# 11  https://www.facebook.com/StKittsHPU/posts/8869...               NaN  
# 12  https://twitter.com/RwandaHealth/status/137518...               NaN  
# 13  https://covid19.moph.gov.qa/EN/Pages/default.aspx               NaN  
# 14  https://www.facebook.com/ntfcovid19ph/posts/29...               NaN  
# 15  https://dghs.gov.bd/images/docs/vpr/Covid-19-V...               NaN  
# 16  https://vacunate.mspbs.gov.py/index-listado-va...               NaN  
# 17  https://covid19.info.gov.pg/index.php/2021/04/...               NaN  
# 18  https://twitter.com/MINSAPma/status/1380301588...               NaN  
# 19  https://eng.belta.by/president/view/vaccinatio...               NaN  
# 20  https://www.dawn.com/news/1617103/govt-to-open...               NaN  