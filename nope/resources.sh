curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php?periode=$waktu | grep "<td bgcolor" -A6 | grep "<td>" | cut -d ">" -f2 | cut -d "<" -f1| sed s/,/./g | sed -e /^$/d > data.txt

curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php?periode=$waktu | grep "96F989" -A13 | grep "<strong>" | cut -d">" -f2 | cut -d"<" -f1 | sed -e /^$/d > upcompanies.txt

curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php?periode=$waktu | grep "FBF14B" -A13 | grep "<strong>" | cut -d">" -f2 | cut -d"<" -f1 | sed -e /^$/d > yellowcompanies.txt

curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php?periode=$waktu | grep "FE848A" -A13 | grep "<strong>" | cut -d">" -f2 | cut -d"<" -f1 | sed -e /^$/d > downcompanies.txt

curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php?periode=$waktu | grep "FBF14B" -A13 | grep "%<" | cut -d ">" -f3 | cut -d "<" -f1 > persenstagnan.txt

curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php?periode=$waktu | grep "96F989" -A13 | grep "%<" | cut -d ">" -f3 | cut -d "<" -f1 > persennaik.txt

curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php?periode=$waktu | grep "FE848A" -A13 | grep "%<" | cut -d ">" -f3 | cut -d "<" -f1 > persenturun.txt
