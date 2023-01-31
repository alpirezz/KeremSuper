import streamlit as st
import pandas as pd
import plotly.express as px
import pymssql


conn = pymssql.connect(server='192.168.171.1',
                       user='sa',
                       password='cZao5X&4&F7&yp83',
                       database='wellbeesV2')
cursor = conn.cursor()


@st.cache(allow_output_mutation=True)
def get_data(sql):
    cursor.execute(sql)
    data = pd.DataFrame.from_records(cursor.fetchall(),
                                     columns=[desc[0] for desc in cursor.description])
    return data

st.set_page_config(layout="wide")
st.title("İYİ Bak Kendine")


st.subheader("İştirak ve lokasyon kırılımlı Total Kullanıcılar")

st.write("Saha")


sorgu=f"""
Select SBName
   , P.Year
   , P.Month
   , CONVERT(decimal, P.UserCount) as UserCount
FROM (Select SBName
      , Year
      , Month
      , (Select COUNT(U2.Id)
       from Users U2
      LEFT JOIN SubBranches SB on U2.SubBranchId = SB.Id
       where U2.CreatedTime < DATEFROMPARTS(Year, Month, 28)
        and U2.Firstname is not null
        and U2.Status = 1
        and U2.CompanyId ='07cc8ede-6800-41bb-87ac-ece0b4008b31'
        and SB.Name = T.SBName
  ) as UserCount
   from (select YEAR(UE.EntryTime) Year,
          MONTH(UE.EntryTime) Month,
          S.Name as SBName
      from Users U
   INNER JOIN UserEntries UE on U.Id = UE.UserId
   LEFT JOIN SubBranches S on U.SubBranchId = S.Id
      where U.CreatedTime is not null
            and U.Id in
           (
select U.Id from Users U
LEFT JOIN SubBranches SB on SB.Id = U.SubBranchId
where SB.Code in (003,004) -- SAHA
--where SB.Code not in (003,004) -- GM
and U.CompanyId='07cc8ede-6800-41bb-87ac-ece0b4008b31'
and U.Status=1
)
      group by YEAR(UE.EntryTime), MONTH(UE.EntryTime),S.Name) AS T
   ) AS P
order by 2,3 desc
"""

dataframe=get_data(sorgu)

print(dataframe)
st.dataframe(dataframe, use_container_width=True)

st.write("Genel Merkez")


sorgu2=f"""
Select SBName
   , P.Year
   , P.Month
   , CONVERT(decimal, P.UserCount) as UserCount
FROM (Select SBName
      , Year
      , Month
      , (Select COUNT(U2.Id)
       from Users U2
      LEFT JOIN SubBranches SB on U2.SubBranchId = SB.Id
       where U2.CreatedTime < DATEFROMPARTS(Year, Month, 28)
        and U2.Firstname is not null
        and U2.Status = 1
        and U2.CompanyId ='07cc8ede-6800-41bb-87ac-ece0b4008b31'
        and SB.Name = T.SBName
  ) as UserCount
   from (select YEAR(UE.EntryTime) Year,
          MONTH(UE.EntryTime) Month,
          S.Name as SBName
      from Users U
   INNER JOIN UserEntries UE on U.Id = UE.UserId
   LEFT JOIN SubBranches S on U.SubBranchId = S.Id
      where U.CreatedTime is not null
            and U.Id in
           (
select U.Id from Users U
LEFT JOIN SubBranches SB on SB.Id = U.SubBranchId
--where SB.Code in (003,004) -- SAHA
where SB.Code not in (003,004) -- GM
and U.CompanyId='07cc8ede-6800-41bb-87ac-ece0b4008b31'
and U.Status=1
)
      group by YEAR(UE.EntryTime), MONTH(UE.EntryTime),S.Name) AS T
   ) AS P
order by 2,3 desc
"""

dataframe2=get_data(sorgu2)

print(dataframe2)
st.dataframe(dataframe2, use_container_width=True)

