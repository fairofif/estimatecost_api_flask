# estimatecost

For END USER:

Untuk mendapatkan token login tokenvalue:

https://wakacipuy.my.id/estimatecost/login (gunakan username = 'mainaccount', password = 'mainaccount')

Estimasi biaya hidup, gaji, uang sisa, berdasarkan kota, role, pengalaman, lifestyle:

https://wakacipuy.my.id/estimatecost/livingcost/CITY/RoleFirstString/RoleSecondString/YearOfExperience/LifeStyleLevel?token=tokenvalue

    - CITY diisi oleh kota yang ada di Germany
    
    - RoleFirstString diisi oleh kata pertama dari posisi kerja (bisa diisi 'f' untuk menonaktifkan filter)
    
    - RoleSecondString diisi oleh kata kedua dari posisi kerja (bisa diisi 'f' untuk menonaktifkan filter)
    
    - YearOfExperience diisi oleh angka berapa lama pengalaman pekerjaan dalam tahun (bisa diisi 'f' untuk menonaktifkan filter)
    
    - LifeStyleLevel diisi salah satu dari (mid/high/low/all)
    
    contoh : https://wakacipuy.my.id/estimatecost/livingcost/Munich/Software/f/f/mid akan mengestimasi cost di kota munich dengan pekerjaan awalan kata software dan lifestyle level menengah
    
Untuk melihat detail cost di kota tertentu (resto, rent, power purchase, groceries):

https://wakacipuy.my.id/estimatecost/allavgcost/CITY/YearOrMonth?token=tokenvalue

    - CITY diisi oleh nama kota
    
    - YearOfMonth diisi oleh year atau month, year untuk cost tahunan, month untuk cost bulanan
  

For Developer User:

Untuk menarik data gaji di germany berdasarkan kota, role, pengalaman, seniorlevel:

http://username:password/@wakacipuy.my.id/estimatecost/login --> return tokenvalue

https://wakacipuy.my.id/estimatecost/getsalaries/city/rolefirst/rolelast/experience/seniorlevel?token=tokenvalue

    - parameter yang bisa null (diisi 'f'): city, rolefirst, rolelast, experience, seniorlevel
    
Untuk menarik data vacation days berdasarkan kota, role, pengalaman, seniorlevel:

http://username:password/@wakacipuy.my.id/estimatecost/login --> return tokenvalue

https://wakacipuy.my.id/getvacationdays/city/rolefirst/rolelast/experience/seniorlevel?token=tokenvalue

    - parameter yang bisa null (diisi 'f'): city, rolefirst, rolelast, experience, seniorlevel
    


