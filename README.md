# Capstone-API-amin

API ini di buat sebagai project akhir dari tim Algoritma selama 1 bulan mengikuti kelas Data Analytic Specialization. DW dilakukan di pandas dan dalam pembuatan API menggunakan Flask dengan IDE Vs Code

Endpoints untuk mendapatkan nama author:
<h2> 1./, method = GET</h2> 

Merupakan endpoint yang bertuju untuk mengambil nama spesific author dari file book_c.csv yg telah di EDA dan Wrangling dengan mengambil nama author spesific, dan akan mengembalikan nama author yang tertuju pada end point tersebut.

<h2> 2./data/get/equal/PGwodehouse/isbn>/value</h2>

Mengembalikan author spesific yang berasal dari file hasil EDA dan Wrangling yang di filter dimana nilai pada isbn = kode buku yang ada pada DF di file spesific author tersebut.

<h2> 3./data/get/lang/Agatha_Christie/language/value</h2>

Mengembalikan buku dari bahasa yang telah di filter dan di save dengan file berbeda dari hasil EDA dan Wrangling dari Author tersebut
